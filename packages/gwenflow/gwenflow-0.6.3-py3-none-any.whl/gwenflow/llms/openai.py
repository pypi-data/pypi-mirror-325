import os
import logging
import json

from typing import Optional, Union, Any, List, Dict
from openai import OpenAI, AsyncOpenAI
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk

from gwenflow.types import ChatCompletionMessage, ChatCompletionMessageToolCall
from gwenflow.llms.base import ChatBase


logger = logging.getLogger(__name__)


class ChatOpenAI(ChatBase):
 
    model: str = "gpt-4o-mini"

    # model parameters
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    n: Optional[int] = None
    stop: Optional[Union[str, List[str]]] = None
    max_completion_tokens: Optional[int] = None
    max_tokens: Optional[int] = None
    presence_penalty: Optional[float] = None
    frequency_penalty: Optional[float] = None
    logit_bias: Optional[Dict[int, float]] = None
    response_format: Optional[Dict[str, Any]] = None
    seed: Optional[int] = None
    logprobs: Optional[bool] = None
    top_logprobs: Optional[int] = None

    # clients
    client: Optional[OpenAI] = None
    async_client: Optional[AsyncOpenAI] = None

    # client parameters
    api_key: Optional[str] = None
    organization: Optional[str] = None
    base_url: Optional[str] = None
    timeout: Optional[Union[float, int]] = None
    max_retries: Optional[int] = None

    def _get_client_params(self) -> Dict[str, Any]:

        api_key = self.api_key
        if api_key is None:
            api_key = os.environ.get("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError(
                "The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable"
            )

        organization = self.organization
        if organization is None:
            organization = os.environ.get('OPENAI_ORG_ID')

        client_params = {
            "api_key": api_key,
            "organization": organization,
            "base_url": self.base_url,
            "timeout": self.timeout,
            "max_retries": self.max_retries,
        }

        client_params = {k: v for k, v in client_params.items() if v is not None}

        return client_params

    @property
    def _get_model_params(self) -> Dict[str, Any]:

        model_params = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "n": self.n,
            "stop": self.stop,
            "max_tokens": self.max_tokens or self.max_completion_tokens,
            "presence_penalty": self.presence_penalty,
            "frequency_penalty": self.frequency_penalty,
            "logit_bias": self.logit_bias,
            "response_format": self.response_format,
            "seed": self.seed,
            "logprobs": self.logprobs,
            "top_logprobs": self.top_logprobs,
        }

        if self.tools:
            tools = [tool.openai_schema for tool in self.tools]
            model_params["tools"] = tools or None
            model_params["tool_choice"] = self.tool_choice or "auto"

        model_params = {k: v for k, v in model_params.items() if v is not None}

        return model_params
    
    def get_client(self) -> OpenAI:

        if self.client:
            return self.client
        
        client_params = self._get_client_params()

        self.client = OpenAI(**client_params)
        return self.client

    def get_async_client(self) -> AsyncOpenAI:

        if self.client:
            return self.client
        
        client_params = self._get_client_params()

        self.async_client = AsyncOpenAI(**client_params)
        return self.async_client

    def _parse_response(self, response, response_format: dict = None):
        """Process the response based on whether tools are used or not."""

        text_response = ""    

        if isinstance(response, ChatCompletionChunk):
            if response.choices[0].delta.content:
                text_response = response.choices[0].delta.content
        else:
            if response.choices[0].message.content:
                text_response = response.choices[0].message.content
        
        if response_format:
            if response_format.get("type") == "json_object":
                text_response = json.loads(text_response)

        return text_response

    def invoke(
        self,
        messages: List[Dict[str, str]],
        parse_response: bool = True,
        **kwargs,
    ):

        response: ChatCompletionMessage = self.get_client().chat.completions.create(
            model=self.model,
            messages=messages,
            **self._get_model_params,
        )

        tool_calls = response.choices[0].message.tool_calls
        if tool_calls and self.tools:
            tool_messages = self.handle_tool_calls(tool_calls=tool_calls)
            if len(tool_messages)>0:
                assistant_message = response.choices[0].message
                messages.append(json.loads(assistant_message.model_dump_json()))
                messages.extend(tool_messages)
                response: ChatCompletionMessage = self.get_client().chat.completions.create(
                    model=self.model,
                    messages=messages,
                    **self._get_model_params,
                )

        if parse_response:
            response = self._parse_response(response, response_format=kwargs.get("response_format"))

        return response

    async def ainvoke(
        self,
        messages: List[Dict[str, str]],
        parse_response: bool = True,
        **kwargs,
    ):

        response: ChatCompletionMessage = await self.get_async_client().chat.completions.create(
            model=self.model,
            messages=messages,
            **self._get_model_params,
        )

        tool_calls = response.choices[0].message.tool_calls
        if tool_calls and self.tools:
            tool_messages = await self.ahandle_tool_calls(tool_calls=tool_calls)
            if len(tool_messages)>0:
                assistant_message = response.choices[0].message
                messages.append(json.loads(assistant_message.model_dump_json()))
                messages.extend(tool_messages)
                response: ChatCompletionMessage = await self.get_async_client().chat.completions.create(
                    model=self.model,
                    messages=messages,
                    **self._get_model_params,
                )

        if parse_response:
            response = self._parse_response(response, response_format=kwargs.get("response_format"))

        return response

    def stream(
        self,
        messages: List[Dict[str, str]],
        parse_response: bool = True,
        **kwargs,
    ):

        response = self.get_client().chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True,
            **self._get_model_params,
        )

        content = ""
        for chunk in response:
            if len(chunk.choices) > 0:
                if chunk.choices[0].finish_reason == "stop":
                    break
                if chunk.choices[0].delta.content:
                    content += chunk.choices[0].delta.content
                if parse_response:
                    chunk = self._parse_response(chunk, response_format=kwargs.get("response_format"))
                yield chunk

    async def astream(
        self,
        messages: List[Dict[str, str]],
        parse_response: bool = True,
        **kwargs,
    ):

        response = await self.get_client().chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True,
            **self._get_model_params,
        )

        content = ""
        async for chunk in response:
            if len(chunk.choices) > 0:
                if chunk.choices[0].finish_reason == "stop":
                    break
                if chunk.choices[0].delta.content:
                    content += chunk.choices[0].delta.content
                if parse_response:
                    chunk = self._parse_response(chunk, response_format=kwargs.get("response_format"))
                yield chunk
 