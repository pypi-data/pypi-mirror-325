from typing import List, Optional, Iterable
from dataclasses import dataclass
from enum import Enum
from functools import wraps

import dacite
import requests

from ai_api_client_sdk.models.status import Status

from gen_ai_hub import GenAIHubProxyClient
from gen_ai_hub.orchestration.exceptions import OrchestrationError
from gen_ai_hub.orchestration.models.base import JSONSerializable
from gen_ai_hub.orchestration.models.config import OrchestrationConfig
from gen_ai_hub.orchestration.models.message import Message
from gen_ai_hub.orchestration.models.template import TemplateValue
from gen_ai_hub.orchestration.models.response import OrchestrationResponse, OrchestrationResponseStreaming
from gen_ai_hub.orchestration.sse_client import SSEClient
from gen_ai_hub.proxy import get_proxy_client


@dataclass
class OrchestrationRequest(JSONSerializable):
    """
    Represents a request for the orchestration process, including configuration, template values, and message history.

    Attributes:
        config: The configuration settings for the orchestration.
        template_values: A list of template values to be used in the request.
        history: The history of messages exchanged, typically used to maintain context.
    """

    config: OrchestrationConfig
    template_values: List[TemplateValue]
    history: List[Message]

    def to_dict(self):
        return {
            "orchestration_config": self.config.to_dict(),
            "input_params": {value.name: value.value for value in self.template_values},
            "messages_history": [message.to_dict() for message in self.history],
        }


def _handle_http_error(error, response):
    if not response.content:
        raise error

    error_content = response.json()

    raise OrchestrationError(
        request_id=error_content.get("request_id"),
        message=error_content.get("message"),
        code=error_content.get("code"),
        location=error_content.get("location"),
        module_results=error_content.get("module_results", {}),
    ) from error


def cache_if_not_none(func):
    """Custom cache decorator that only caches non-None results"""
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))  # Create hashable key for cache
        if key not in cache:
            result = func(*args, **kwargs)
            if result is not None:  # Only cache if result is not None
                cache[key] = result
            return result
        return cache[key]

    def cache_clear():
        cache.clear()

    wrapper.cache_clear = cache_clear
    return wrapper

# pylint: disable=too-many-arguments,too-many-positional-arguments
@cache_if_not_none
def _get_orchestration_api_url(base_url: str,
                               auth_url: str,
                               client_id: str,
                               client_secret: str,
                               resource_group: str,
                               config_id: Optional[str] = None,
                               config_name: Optional[str] = None,
                               orchestration_scenario: str = "orchestration",
                               executable_id: str = "orchestration"):
    proxy_client = GenAIHubProxyClient(
        base_url=base_url,
        auth_url=auth_url,
        client_id=client_id,
        client_secret=client_secret,
        resource_group=resource_group,
    )
    deployments = proxy_client.ai_core_client.deployment.query(
        scenario_id=orchestration_scenario,
        executable_ids=[executable_id],
        status=Status.RUNNING
    )
    if deployments.count > 0:
        sorted_deployments = sorted(deployments.resources, key=lambda x: x.start_time)[::-1]
        check_for = {}
        if config_name:
            check_for["configuration_name"] = config_name
        if config_id:
            check_for["configuration_id"] = config_id
        if not check_for:
            return sorted_deployments[0].deployment_url
        for deployment in sorted_deployments:
            if all(getattr(deployment, key) == value for key, value in check_for.items()):
                return deployment.deployment_url
    return None

def get_orchestration_api_url(proxy_client: GenAIHubProxyClient,
                              deployment_id: Optional[str] = None,
                              config_name: Optional[str] = None,
                              config_id: Optional[str] = None) -> str:
    if deployment_id:
        return f"{proxy_client.ai_core_client.base_url.rstrip('/')}/inference/deployments/{deployment_id}"
    url = _get_orchestration_api_url(
        **proxy_client.model_dump(exclude='ai_core_client'),
        config_name=config_name,
        config_id=config_id
    )
    if url is None:
        raise ValueError('No Orchestration deployment found!')
    return url


class OrchestrationService:
    """
    A service for executing orchestration requests, allowing for the generation of LLM-generated content
    through a pipeline of configured modules.

    Attributes:
        api_url: The base URL for the orchestration API, through which all requests are made.
        config: An optional default configuration for the orchestration pipeline, which can be overridden per request.
        proxy_client: An optional proxy client for managing HTTP requests, facilitating communication with the API.
    """

    def __init__(
        self,
        api_url: Optional[str] = None,
        config: Optional[OrchestrationConfig] = None,
        proxy_client: Optional[GenAIHubProxyClient] = None,
        deployment_id: Optional[str] = None,
        config_name: Optional[str] = None,
        config_id: Optional[str] = None,
    ):
        self.proxy_client = proxy_client or get_proxy_client(proxy_version="gen-ai-hub")
        self.api_url = api_url or get_orchestration_api_url(
            self.proxy_client,
            deployment_id=deployment_id,
            config_name=config_name,
            config_id=config_id
        )
        self.config = config

    def _execute_request(
        self,
        config: OrchestrationConfig,
        template_values: List[TemplateValue],
        history: List[Message],
        stream: bool,
        stream_options: Optional[dict] = None
    ) -> OrchestrationResponse or Iterable[OrchestrationResponse]:
        if config is None:
            raise ValueError("A configuration is required to invoke the orchestration service.")

        config._stream = stream
        if stream_options:
            config.stream_options = stream_options

        request = OrchestrationRequest(
            config=config,
            template_values=template_values or [],
            history=history or [],
        )

        response = requests.post(
            self.api_url + "/completion",
            headers=self.proxy_client.request_header,
            json=request.to_dict(),
            stream=stream
        )

        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            _handle_http_error(error, response)

        if stream:
            return SSEClient(response)

        return dacite.from_dict(
            data_class=OrchestrationResponse,
            data=response.json(),
            config=dacite.Config(cast=[Enum]),
        )

    def run(
        self,
        config: Optional[OrchestrationConfig] = None,
        template_values: Optional[List[TemplateValue]] = None,
        history: Optional[List[Message]] = None,
    ) -> OrchestrationResponse:
        """
            Executes an orchestration request synchronously, combining various modules into a pipeline
            and generating a complete response.

            Args:
                config: The configuration for this orchestration run. If not provided, the default
                    configuration set during initialization will be used.
                template_values: A list of key-value pairs to populate the request templates,
                    allowing dynamic input.
                history: The message history, maintaining context across multiple interactions.

            Raises:
                ValueError: If no configuration is provided either during initialization or in
                    the method call, as the orchestration cannot be executed without it.
                OrchestrationError: If the API request fails due to an HTTP error, with details
                    provided by the service's error response.
        """
        return self._execute_request(
            config=config or self.config,
            template_values=template_values,
            history=history,
            stream=False
        )

    def stream(
        self,
        config: Optional[OrchestrationConfig] = None,
        template_values: Optional[List[TemplateValue]] = None,
        history: Optional[List[Message]] = None,
        stream_options: Optional[dict] = None,
    ) -> Iterable[OrchestrationResponseStreaming]:
        """
            Executes an orchestration request in streaming mode, yielding partial responses
            as they become available.

            Args:
                config: The configuration for this orchestration run. If not provided, the default
                    configuration set during initialization will be used.
                template_values: A list of key-value pairs to populate the request templates,
                    allowing dynamic input.
                history: The message history, maintaining context across multiple interactions.
                stream_options: Additional options to configure the streaming behavior. See
                    documentation for available options.

            Raises:
                ValueError: If no configuration is provided either during initialization or in
                    the method call, as the orchestration cannot be executed without it.
                OrchestrationError: If the API request fails due to an HTTP error, with details
                    provided by the service's error response.
        """
        return self._execute_request(
            config=config or self.config,
            template_values=template_values,
            history=history,
            stream=True,
            stream_options=stream_options
        )
