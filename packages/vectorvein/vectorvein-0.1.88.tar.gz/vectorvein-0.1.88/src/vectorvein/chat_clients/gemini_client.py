# @Author: Bi Ying
# @Date:   2024-06-17 23:47:49
import json
from functools import cached_property
from typing import Iterable, Literal, Generator, AsyncGenerator, overload, Any

import httpx

from .utils import cutoff_messages
from ..types import defaults as defs
from .base_client import BaseChatClient, BaseAsyncChatClient
from ..types.enums import ContextLengthControlType, BackendType
from ..types.llm_parameters import (
    NotGiven,
    NOT_GIVEN,
    ToolParam,
    ToolChoice,
    ChatCompletionMessage,
    ChatCompletionDeltaMessage,
    ChatCompletionStreamOptionsParam,
)


class GeminiChatClient(BaseChatClient):
    DEFAULT_MODEL: str = defs.GEMINI_DEFAULT_MODEL
    BACKEND_NAME: BackendType = BackendType.Gemini

    def __init__(
        self,
        model: str = defs.GEMINI_DEFAULT_MODEL,
        stream: bool = True,
        temperature: float | None | NotGiven = NOT_GIVEN,
        context_length_control: ContextLengthControlType = defs.CONTEXT_LENGTH_CONTROL,
        random_endpoint: bool = True,
        endpoint_id: str = "",
        http_client: httpx.Client | None = None,
        backend_name: str | None = None,
    ):
        super().__init__(
            model,
            stream,
            temperature,
            context_length_control,
            random_endpoint,
            endpoint_id,
            http_client,
            backend_name,
        )
        self.model_id = None
        self.endpoint = None

    @cached_property
    def raw_client(self):
        self.endpoint, self.model_id = self._set_endpoint()
        if not self.http_client:
            self.http_client = httpx.Client(timeout=300, proxy=self.endpoint.proxy)
        return self.http_client

    @overload
    def create_completion(
        self,
        *,
        messages: list,
        model: str | None = None,
        stream: Literal[False] = False,
        temperature: float | None | NotGiven = NOT_GIVEN,
        max_tokens: int | None = None,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        response_format: dict | None = None,
        stream_options: ChatCompletionStreamOptionsParam | None = None,
        top_p: float | NotGiven | None = NOT_GIVEN,
        skip_cutoff: bool = False,
        **kwargs,
    ) -> ChatCompletionMessage:
        pass

    @overload
    def create_completion(
        self,
        *,
        messages: list,
        model: str | None = None,
        stream: Literal[True],
        temperature: float | None | NotGiven = NOT_GIVEN,
        max_tokens: int | None = None,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        response_format: dict | None = None,
        stream_options: ChatCompletionStreamOptionsParam | None = None,
        top_p: float | NotGiven | None = NOT_GIVEN,
        skip_cutoff: bool = False,
        **kwargs,
    ) -> Generator[ChatCompletionDeltaMessage, None, None]:
        pass

    @overload
    def create_completion(
        self,
        *,
        messages: list,
        model: str | None = None,
        stream: bool,
        temperature: float | None | NotGiven = NOT_GIVEN,
        max_tokens: int | None = None,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        response_format: dict | None = None,
        stream_options: ChatCompletionStreamOptionsParam | None = None,
        top_p: float | NotGiven | None = NOT_GIVEN,
        skip_cutoff: bool = False,
        **kwargs,
    ) -> ChatCompletionMessage | Generator[ChatCompletionDeltaMessage, Any, None]:
        pass

    def create_completion(
        self,
        *,
        messages: list,
        model: str | None = None,
        stream: Literal[False] | Literal[True] = False,
        temperature: float | None | NotGiven = NOT_GIVEN,
        max_tokens: int | None = None,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        response_format: dict | None = None,
        stream_options: ChatCompletionStreamOptionsParam | None = None,
        top_p: float | NotGiven | None = NOT_GIVEN,
        skip_cutoff: bool = False,
        **kwargs,
    ):
        if model is not None:
            self.model = model
        if stream is not None:
            self.stream = stream
        if temperature is not None:
            self.temperature = temperature

        self.model_setting = self.backend_settings.models[self.model]
        if self.model_id is None:
            self.model_id = self.model_setting.id

        self.endpoint, self.model_id = self._set_endpoint()

        if messages[0].get("role") == "system":
            system_prompt = messages[0]["content"]
            messages = messages[1:]
        else:
            system_prompt = ""

        if not skip_cutoff and self.context_length_control == ContextLengthControlType.Latest:
            messages = cutoff_messages(
                messages,
                max_count=self.model_setting.context_length,
                backend=self.BACKEND_NAME,
                model=self.model_setting.id,
            )

        tools_params = {}
        if tools:
            tools_params = {"tools": [{"function_declarations": [tool["function"] for tool in tools]}]}

        response_format_params = {}
        if response_format is not None:
            if response_format.get("type") == "json_object":
                response_format_params = {"response_mime_type": "application/json"}

        top_p_params = {}
        if top_p:
            top_p_params = {"top_p": top_p}

        temperature_params = {}
        if temperature:
            temperature_params = {"temperature": temperature}

        request_body = {
            "contents": messages,
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_ONLY_HIGH",
                }
            ],
            "generationConfig": {
                "maxOutputTokens": max_tokens,
                **temperature_params,
                **top_p_params,
                **response_format_params,
            },
            **tools_params,
            **kwargs,
        }
        if system_prompt:
            request_body["systemInstruction"] = {"parts": [{"text": system_prompt}]}

        headers = {"Content-Type": "application/json"}

        params = {"key": self.endpoint.api_key}

        if self.stream:
            url = f"{self.endpoint.api_base}/models/{self.model_setting.id}:streamGenerateContent"
            params["alt"] = "sse"

            def generator():
                result = {"content": "", "tool_calls": [], "usage": {}}
                client = self.raw_client
                with client.stream("POST", url, headers=headers, params=params, json=request_body) as response:
                    for chunk in response.iter_lines():
                        message = {"content": "", "tool_calls": []}
                        if not chunk.startswith("data:"):
                            continue
                        data = json.loads(chunk[5:])
                        chunk_content = data["candidates"][0]["content"]["parts"][0]
                        if "text" in chunk_content:
                            message["content"] = chunk_content["text"]
                            result["content"] += message["content"]
                        elif "functionCall" in chunk_content:
                            message["tool_calls"] = [
                                {
                                    "index": 0,
                                    "id": "call_0",
                                    "function": {
                                        "arguments": json.dumps(
                                            chunk_content["functionCall"]["args"], ensure_ascii=False
                                        ),
                                        "name": chunk_content["functionCall"]["name"],
                                    },
                                    "type": "function",
                                }
                            ]

                        result["usage"] = message["usage"] = {
                            "prompt_tokens": data["usageMetadata"].get("promptTokenCount", 0),
                            "completion_tokens": data["usageMetadata"].get("candidatesTokenCount", 0),
                            "total_tokens": data["usageMetadata"].get("totalTokenCount", 0),
                        }
                        yield ChatCompletionDeltaMessage(**message)

            return generator()
        else:
            url = f"{self.endpoint.api_base}/models/{self.model_setting.id}:generateContent"
            client = self.raw_client
            response = client.post(url, json=request_body, headers=headers, params=params, timeout=None).json()
            if "error" in response:
                raise Exception(response["error"])
            result = {
                "content": "",
                "usage": {
                    "prompt_tokens": response.get("usageMetadata", {}).get("promptTokenCount", 0),
                    "completion_tokens": response.get("usageMetadata", {}).get("candidatesTokenCount", 0),
                    "total_tokens": response.get("usageMetadata", {}).get("totalTokenCount", 0),
                },
            }
            tool_calls = []
            for part in response["candidates"][0]["content"]["parts"]:
                if "text" in part:
                    result["content"] += part["text"]
                elif "functionCall" in part:
                    tool_call = {
                        "index": 0,
                        "id": "call_0",
                        "function": {
                            "arguments": json.dumps(part["functionCall"]["args"], ensure_ascii=False),
                            "name": part["functionCall"]["name"],
                        },
                        "type": "function",
                    }
                    tool_calls.append(tool_call)

            if tool_calls:
                result["tool_calls"] = tool_calls

            return ChatCompletionMessage(**result)


class AsyncGeminiChatClient(BaseAsyncChatClient):
    DEFAULT_MODEL: str = defs.GEMINI_DEFAULT_MODEL
    BACKEND_NAME: BackendType = BackendType.Gemini

    def __init__(
        self,
        model: str = defs.GEMINI_DEFAULT_MODEL,
        stream: bool = True,
        temperature: float | None | NotGiven = NOT_GIVEN,
        context_length_control: ContextLengthControlType = defs.CONTEXT_LENGTH_CONTROL,
        random_endpoint: bool = True,
        endpoint_id: str = "",
        http_client: httpx.AsyncClient | None = None,
        backend_name: str | None = None,
    ):
        super().__init__(
            model,
            stream,
            temperature,
            context_length_control,
            random_endpoint,
            endpoint_id,
            http_client,
            backend_name,
        )
        self.model_id = None
        self.endpoint = None

    @cached_property
    def raw_client(self):
        self.endpoint, self.model_id = self._set_endpoint()
        if not self.http_client:
            self.http_client = httpx.AsyncClient(timeout=300, proxy=self.endpoint.proxy)
        return self.http_client

    @overload
    async def create_completion(
        self,
        *,
        messages: list,
        model: str | None = None,
        stream: Literal[False] = False,
        temperature: float | None | NotGiven = NOT_GIVEN,
        max_tokens: int | None = None,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        response_format: dict | None = None,
        stream_options: ChatCompletionStreamOptionsParam | None = None,
        top_p: float | NotGiven | None = NOT_GIVEN,
        skip_cutoff: bool = False,
        **kwargs,
    ) -> ChatCompletionMessage:
        pass

    @overload
    async def create_completion(
        self,
        *,
        messages: list,
        model: str | None = None,
        stream: Literal[True],
        temperature: float | None | NotGiven = NOT_GIVEN,
        max_tokens: int | None = None,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        response_format: dict | None = None,
        stream_options: ChatCompletionStreamOptionsParam | None = None,
        top_p: float | NotGiven | None = NOT_GIVEN,
        skip_cutoff: bool = False,
        **kwargs,
    ) -> AsyncGenerator[ChatCompletionDeltaMessage, Any]:
        pass

    @overload
    async def create_completion(
        self,
        *,
        messages: list,
        model: str | None = None,
        stream: bool,
        temperature: float | None | NotGiven = NOT_GIVEN,
        max_tokens: int | None = None,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        response_format: dict | None = None,
        stream_options: ChatCompletionStreamOptionsParam | None = None,
        top_p: float | NotGiven | None = NOT_GIVEN,
        skip_cutoff: bool = False,
        **kwargs,
    ) -> ChatCompletionMessage | AsyncGenerator[ChatCompletionDeltaMessage, Any]:
        pass

    async def create_completion(
        self,
        *,
        messages: list,
        model: str | None = None,
        stream: Literal[False] | Literal[True] = False,
        temperature: float | None | NotGiven = NOT_GIVEN,
        max_tokens: int | None = None,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        response_format: dict | None = None,
        stream_options: ChatCompletionStreamOptionsParam | None = None,
        top_p: float | NotGiven | None = NOT_GIVEN,
        skip_cutoff: bool = False,
        **kwargs,
    ):
        if model is not None:
            self.model = model
        if stream is not None:
            self.stream = stream
        if temperature is not None:
            self.temperature = temperature

        self.model_setting = self.backend_settings.models[self.model]
        if self.model_id is None:
            self.model_id = self.model_setting.id

        self.endpoint, self.model_id = self._set_endpoint()

        if messages[0].get("role") == "system":
            system_prompt = messages[0]["content"]
            messages = messages[1:]
        else:
            system_prompt = ""

        if not skip_cutoff and self.context_length_control == ContextLengthControlType.Latest:
            messages = cutoff_messages(
                messages,
                max_count=self.model_setting.context_length,
                backend=self.BACKEND_NAME,
                model=self.model_setting.id,
            )

        tools_params = {}
        if tools:
            tools_params = {"tools": [{"function_declarations": [tool["function"] for tool in tools]}]}

        response_format_params = {}
        if response_format is not None:
            if response_format.get("type") == "json_object":
                response_format_params = {"response_mime_type": "application/json"}

        top_p_params = {}
        if top_p:
            top_p_params = {"top_p": top_p}

        temperature_params = {}
        if temperature:
            temperature_params = {"temperature": temperature}

        request_body = {
            "contents": messages,
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_ONLY_HIGH",
                }
            ],
            "generationConfig": {
                "maxOutputTokens": max_tokens,
                **temperature_params,
                **top_p_params,
                **response_format_params,
            },
            **tools_params,
            **kwargs,
        }
        if system_prompt:
            request_body["systemInstruction"] = {"parts": [{"text": system_prompt}]}

        headers = {"Content-Type": "application/json"}

        params = {"key": self.endpoint.api_key}

        if self.stream:
            url = f"{self.endpoint.api_base}/models/{self.model_setting.id}:streamGenerateContent"
            params["alt"] = "sse"

            async def generator():
                result = {"content": "", "tool_calls": [], "usage": {}}
                client = self.raw_client
                async with client.stream("POST", url, headers=headers, params=params, json=request_body) as response:
                    async for chunk in response.aiter_lines():
                        message = {"content": "", "tool_calls": []}
                        if not chunk.startswith("data:"):
                            continue
                        data = json.loads(chunk[5:])
                        chunk_content = data["candidates"][0]["content"]["parts"][0]
                        if "text" in chunk_content:
                            message["content"] = chunk_content["text"]
                            result["content"] += message["content"]
                        elif "functionCall" in chunk_content:
                            message["tool_calls"] = [
                                {
                                    "index": 0,
                                    "id": "call_0",
                                    "function": {
                                        "arguments": json.dumps(
                                            chunk_content["functionCall"]["args"], ensure_ascii=False
                                        ),
                                        "name": chunk_content["functionCall"]["name"],
                                    },
                                    "type": "function",
                                }
                            ]

                        result["usage"] = message["usage"] = {
                            "prompt_tokens": data["usageMetadata"].get("promptTokenCount", 0),
                            "completion_tokens": data["usageMetadata"].get("candidatesTokenCount", 0),
                            "total_tokens": data["usageMetadata"].get("totalTokenCount", 0),
                        }
                        yield ChatCompletionDeltaMessage(**message)

            return generator()
        else:
            url = f"{self.endpoint.api_base}/models/{self.model_setting.id}:generateContent"
            client = self.raw_client
            async with client:
                response = await client.post(url, json=request_body, headers=headers, params=params, timeout=None)
                response = response.json()
                if "error" in response:
                    raise Exception(response["error"])
                result = {
                    "content": "",
                    "usage": {
                        "prompt_tokens": response.get("usageMetadata", {}).get("promptTokenCount", 0),
                        "completion_tokens": response.get("usageMetadata", {}).get("candidatesTokenCount", 0),
                        "total_tokens": response.get("usageMetadata", {}).get("totalTokenCount", 0),
                    },
                }
                tool_calls = []
                for part in response["candidates"][0]["content"]["parts"]:
                    if "text" in part:
                        result["content"] += part["text"]
                    elif "functionCall" in part:
                        tool_call = {
                            "index": 0,
                            "id": "call_0",
                            "function": {
                                "arguments": json.dumps(part["functionCall"]["args"], ensure_ascii=False),
                                "name": part["functionCall"]["name"],
                            },
                            "type": "function",
                        }
                        tool_calls.append(tool_call)

                if tool_calls:
                    result["tool_calls"] = tool_calls

                return ChatCompletionMessage(**result)
