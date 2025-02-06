# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.models import completion_create_params
from ...types.parameter_bindings_param import ParameterBindingsParam
from ...types.shared.completion_response import CompletionResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scaleapi/sgp-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scaleapi/sgp-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        model_deployment_id: str,
        *,
        prompt: str,
        chat_template: str | NotGiven = NOT_GIVEN,
        chat_template_kwargs: object | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_request_parameters: ParameterBindingsParam | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse:
        """
        ### Description

        Interact with the LLM model using the specified model_deployment_id. The LLM
        model will generate a text completion based on the provided prompt.

        ```json
        {
          "prompt": "What is the capital of France?"
        }
        ```

        Args:
          chat_template: The chat template to use for the completion. Currently only supported for
              llmengine chat models.

          chat_template_kwargs: Additional keyword arguments for the chat template. Currently only supported for
              llmengine chat models.

          frequency_penalty: Penalize tokens based on how much they have already appeared in the text.
              Positive values encourage the model to generate new tokens and negative values
              encourage the model to repeat tokens. Available for models provided by LLM
              Engine and OpenAI.

          logprobs: Whether to return logprobs. Currently only supported for llmengine chat models.

          max_tokens: The maximum number of tokens to generate in the completion. The token count of
              your prompt plus max_tokens cannot exceed the model's context length. If not,
              specified, max_tokens will be determined based on the model used: | Model API
              family | Model API default | EGP applied default | | --- | --- | --- | | OpenAI
              Completions |
              [`16`](https://platform.openai.com/docs/api-reference/completions/create#max_tokens)
              | `context window - prompt size` | | OpenAI Chat Completions |
              [`context window - prompt size`](https://platform.openai.com/docs/api-reference/chat/create#max_tokens)
              | `context window - prompt size` | | LLM Engine |
              [`max_new_tokens`](https://github.com/scaleapi/launch-python-client/blob/207adced1c88c1c2907266fa9dd1f1ff3ec0ea5b/launch/client.py#L2910)
              parameter is required | `100` | | Anthropic Claude 2 |
              [`max_tokens_to_sample`](https://docs.anthropic.com/claude/reference/complete_post)
              parameter is required | `10000` |

          presence_penalty: Penalize tokens based on if they have already appeared in the text. Positive
              values encourage the model to generate new tokens and negative values encourage
              the model to repeat tokens. Available for models provided by LLM Engine and
              OpenAI.

          stop_sequences: List of up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream: Flag indicating whether to stream the completion response

          temperature: What sampling temperature to use, between [0, 2]. Higher values like 1.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. Setting temperature=0.0 will enable fully
              deterministic (greedy) sampling.NOTE: The temperature parameter range for some
              model is limited to [0, 1] if the given value is above the available range, it
              defaults to the max value.

          top_k: Sample from the k most likely next tokens at each step. Lower k focuses on
              higher probability tokens. Available for models provided by Google and LLM
              Engine.

          top_logprobs: Number of top logprobs to return. Currently only supported for llmengine chat
              models.

          top_p: The cumulative probability cutoff for token selection. Lower values mean
              sampling from a smaller, more top-weighted nucleus. Available for models
              provided by Google, LLM Engine, and OpenAI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        model_deployment_id: str,
        *,
        prompt: str,
        stream: Literal[True],
        chat_template: str | NotGiven = NOT_GIVEN,
        chat_template_kwargs: object | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_request_parameters: ParameterBindingsParam | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[CompletionResponse]:
        """
        ### Description

        Interact with the LLM model using the specified model_deployment_id. The LLM
        model will generate a text completion based on the provided prompt.

        ```json
        {
          "prompt": "What is the capital of France?"
        }
        ```

        Args:
          stream: Flag indicating whether to stream the completion response

          chat_template: The chat template to use for the completion. Currently only supported for
              llmengine chat models.

          chat_template_kwargs: Additional keyword arguments for the chat template. Currently only supported for
              llmengine chat models.

          frequency_penalty: Penalize tokens based on how much they have already appeared in the text.
              Positive values encourage the model to generate new tokens and negative values
              encourage the model to repeat tokens. Available for models provided by LLM
              Engine and OpenAI.

          logprobs: Whether to return logprobs. Currently only supported for llmengine chat models.

          max_tokens: The maximum number of tokens to generate in the completion. The token count of
              your prompt plus max_tokens cannot exceed the model's context length. If not,
              specified, max_tokens will be determined based on the model used: | Model API
              family | Model API default | EGP applied default | | --- | --- | --- | | OpenAI
              Completions |
              [`16`](https://platform.openai.com/docs/api-reference/completions/create#max_tokens)
              | `context window - prompt size` | | OpenAI Chat Completions |
              [`context window - prompt size`](https://platform.openai.com/docs/api-reference/chat/create#max_tokens)
              | `context window - prompt size` | | LLM Engine |
              [`max_new_tokens`](https://github.com/scaleapi/launch-python-client/blob/207adced1c88c1c2907266fa9dd1f1ff3ec0ea5b/launch/client.py#L2910)
              parameter is required | `100` | | Anthropic Claude 2 |
              [`max_tokens_to_sample`](https://docs.anthropic.com/claude/reference/complete_post)
              parameter is required | `10000` |

          presence_penalty: Penalize tokens based on if they have already appeared in the text. Positive
              values encourage the model to generate new tokens and negative values encourage
              the model to repeat tokens. Available for models provided by LLM Engine and
              OpenAI.

          stop_sequences: List of up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          temperature: What sampling temperature to use, between [0, 2]. Higher values like 1.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. Setting temperature=0.0 will enable fully
              deterministic (greedy) sampling.NOTE: The temperature parameter range for some
              model is limited to [0, 1] if the given value is above the available range, it
              defaults to the max value.

          top_k: Sample from the k most likely next tokens at each step. Lower k focuses on
              higher probability tokens. Available for models provided by Google and LLM
              Engine.

          top_logprobs: Number of top logprobs to return. Currently only supported for llmengine chat
              models.

          top_p: The cumulative probability cutoff for token selection. Lower values mean
              sampling from a smaller, more top-weighted nucleus. Available for models
              provided by Google, LLM Engine, and OpenAI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        model_deployment_id: str,
        *,
        prompt: str,
        stream: bool,
        chat_template: str | NotGiven = NOT_GIVEN,
        chat_template_kwargs: object | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_request_parameters: ParameterBindingsParam | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse | Stream[CompletionResponse]:
        """
        ### Description

        Interact with the LLM model using the specified model_deployment_id. The LLM
        model will generate a text completion based on the provided prompt.

        ```json
        {
          "prompt": "What is the capital of France?"
        }
        ```

        Args:
          stream: Flag indicating whether to stream the completion response

          chat_template: The chat template to use for the completion. Currently only supported for
              llmengine chat models.

          chat_template_kwargs: Additional keyword arguments for the chat template. Currently only supported for
              llmengine chat models.

          frequency_penalty: Penalize tokens based on how much they have already appeared in the text.
              Positive values encourage the model to generate new tokens and negative values
              encourage the model to repeat tokens. Available for models provided by LLM
              Engine and OpenAI.

          logprobs: Whether to return logprobs. Currently only supported for llmengine chat models.

          max_tokens: The maximum number of tokens to generate in the completion. The token count of
              your prompt plus max_tokens cannot exceed the model's context length. If not,
              specified, max_tokens will be determined based on the model used: | Model API
              family | Model API default | EGP applied default | | --- | --- | --- | | OpenAI
              Completions |
              [`16`](https://platform.openai.com/docs/api-reference/completions/create#max_tokens)
              | `context window - prompt size` | | OpenAI Chat Completions |
              [`context window - prompt size`](https://platform.openai.com/docs/api-reference/chat/create#max_tokens)
              | `context window - prompt size` | | LLM Engine |
              [`max_new_tokens`](https://github.com/scaleapi/launch-python-client/blob/207adced1c88c1c2907266fa9dd1f1ff3ec0ea5b/launch/client.py#L2910)
              parameter is required | `100` | | Anthropic Claude 2 |
              [`max_tokens_to_sample`](https://docs.anthropic.com/claude/reference/complete_post)
              parameter is required | `10000` |

          presence_penalty: Penalize tokens based on if they have already appeared in the text. Positive
              values encourage the model to generate new tokens and negative values encourage
              the model to repeat tokens. Available for models provided by LLM Engine and
              OpenAI.

          stop_sequences: List of up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          temperature: What sampling temperature to use, between [0, 2]. Higher values like 1.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. Setting temperature=0.0 will enable fully
              deterministic (greedy) sampling.NOTE: The temperature parameter range for some
              model is limited to [0, 1] if the given value is above the available range, it
              defaults to the max value.

          top_k: Sample from the k most likely next tokens at each step. Lower k focuses on
              higher probability tokens. Available for models provided by Google and LLM
              Engine.

          top_logprobs: Number of top logprobs to return. Currently only supported for llmengine chat
              models.

          top_p: The cumulative probability cutoff for token selection. Lower values mean
              sampling from a smaller, more top-weighted nucleus. Available for models
              provided by Google, LLM Engine, and OpenAI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["prompt"], ["prompt", "stream"])
    def create(
        self,
        model_deployment_id: str,
        *,
        prompt: str,
        chat_template: str | NotGiven = NOT_GIVEN,
        chat_template_kwargs: object | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_request_parameters: ParameterBindingsParam | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse | Stream[CompletionResponse]:
        if not model_deployment_id:
            raise ValueError(
                f"Expected a non-empty value for `model_deployment_id` but received {model_deployment_id!r}"
            )
        return self._post(
            f"/v4/models/{model_deployment_id}/completions",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "chat_template": chat_template,
                    "chat_template_kwargs": chat_template_kwargs,
                    "frequency_penalty": frequency_penalty,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "model_request_parameters": model_request_parameters,
                    "presence_penalty": presence_penalty,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionResponse,
            stream=stream or False,
            stream_cls=Stream[CompletionResponse],
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/scaleapi/sgp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/scaleapi/sgp-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        model_deployment_id: str,
        *,
        prompt: str,
        chat_template: str | NotGiven = NOT_GIVEN,
        chat_template_kwargs: object | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_request_parameters: ParameterBindingsParam | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse:
        """
        ### Description

        Interact with the LLM model using the specified model_deployment_id. The LLM
        model will generate a text completion based on the provided prompt.

        ```json
        {
          "prompt": "What is the capital of France?"
        }
        ```

        Args:
          chat_template: The chat template to use for the completion. Currently only supported for
              llmengine chat models.

          chat_template_kwargs: Additional keyword arguments for the chat template. Currently only supported for
              llmengine chat models.

          frequency_penalty: Penalize tokens based on how much they have already appeared in the text.
              Positive values encourage the model to generate new tokens and negative values
              encourage the model to repeat tokens. Available for models provided by LLM
              Engine and OpenAI.

          logprobs: Whether to return logprobs. Currently only supported for llmengine chat models.

          max_tokens: The maximum number of tokens to generate in the completion. The token count of
              your prompt plus max_tokens cannot exceed the model's context length. If not,
              specified, max_tokens will be determined based on the model used: | Model API
              family | Model API default | EGP applied default | | --- | --- | --- | | OpenAI
              Completions |
              [`16`](https://platform.openai.com/docs/api-reference/completions/create#max_tokens)
              | `context window - prompt size` | | OpenAI Chat Completions |
              [`context window - prompt size`](https://platform.openai.com/docs/api-reference/chat/create#max_tokens)
              | `context window - prompt size` | | LLM Engine |
              [`max_new_tokens`](https://github.com/scaleapi/launch-python-client/blob/207adced1c88c1c2907266fa9dd1f1ff3ec0ea5b/launch/client.py#L2910)
              parameter is required | `100` | | Anthropic Claude 2 |
              [`max_tokens_to_sample`](https://docs.anthropic.com/claude/reference/complete_post)
              parameter is required | `10000` |

          presence_penalty: Penalize tokens based on if they have already appeared in the text. Positive
              values encourage the model to generate new tokens and negative values encourage
              the model to repeat tokens. Available for models provided by LLM Engine and
              OpenAI.

          stop_sequences: List of up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream: Flag indicating whether to stream the completion response

          temperature: What sampling temperature to use, between [0, 2]. Higher values like 1.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. Setting temperature=0.0 will enable fully
              deterministic (greedy) sampling.NOTE: The temperature parameter range for some
              model is limited to [0, 1] if the given value is above the available range, it
              defaults to the max value.

          top_k: Sample from the k most likely next tokens at each step. Lower k focuses on
              higher probability tokens. Available for models provided by Google and LLM
              Engine.

          top_logprobs: Number of top logprobs to return. Currently only supported for llmengine chat
              models.

          top_p: The cumulative probability cutoff for token selection. Lower values mean
              sampling from a smaller, more top-weighted nucleus. Available for models
              provided by Google, LLM Engine, and OpenAI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        model_deployment_id: str,
        *,
        prompt: str,
        stream: Literal[True],
        chat_template: str | NotGiven = NOT_GIVEN,
        chat_template_kwargs: object | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_request_parameters: ParameterBindingsParam | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[CompletionResponse]:
        """
        ### Description

        Interact with the LLM model using the specified model_deployment_id. The LLM
        model will generate a text completion based on the provided prompt.

        ```json
        {
          "prompt": "What is the capital of France?"
        }
        ```

        Args:
          stream: Flag indicating whether to stream the completion response

          chat_template: The chat template to use for the completion. Currently only supported for
              llmengine chat models.

          chat_template_kwargs: Additional keyword arguments for the chat template. Currently only supported for
              llmengine chat models.

          frequency_penalty: Penalize tokens based on how much they have already appeared in the text.
              Positive values encourage the model to generate new tokens and negative values
              encourage the model to repeat tokens. Available for models provided by LLM
              Engine and OpenAI.

          logprobs: Whether to return logprobs. Currently only supported for llmengine chat models.

          max_tokens: The maximum number of tokens to generate in the completion. The token count of
              your prompt plus max_tokens cannot exceed the model's context length. If not,
              specified, max_tokens will be determined based on the model used: | Model API
              family | Model API default | EGP applied default | | --- | --- | --- | | OpenAI
              Completions |
              [`16`](https://platform.openai.com/docs/api-reference/completions/create#max_tokens)
              | `context window - prompt size` | | OpenAI Chat Completions |
              [`context window - prompt size`](https://platform.openai.com/docs/api-reference/chat/create#max_tokens)
              | `context window - prompt size` | | LLM Engine |
              [`max_new_tokens`](https://github.com/scaleapi/launch-python-client/blob/207adced1c88c1c2907266fa9dd1f1ff3ec0ea5b/launch/client.py#L2910)
              parameter is required | `100` | | Anthropic Claude 2 |
              [`max_tokens_to_sample`](https://docs.anthropic.com/claude/reference/complete_post)
              parameter is required | `10000` |

          presence_penalty: Penalize tokens based on if they have already appeared in the text. Positive
              values encourage the model to generate new tokens and negative values encourage
              the model to repeat tokens. Available for models provided by LLM Engine and
              OpenAI.

          stop_sequences: List of up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          temperature: What sampling temperature to use, between [0, 2]. Higher values like 1.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. Setting temperature=0.0 will enable fully
              deterministic (greedy) sampling.NOTE: The temperature parameter range for some
              model is limited to [0, 1] if the given value is above the available range, it
              defaults to the max value.

          top_k: Sample from the k most likely next tokens at each step. Lower k focuses on
              higher probability tokens. Available for models provided by Google and LLM
              Engine.

          top_logprobs: Number of top logprobs to return. Currently only supported for llmengine chat
              models.

          top_p: The cumulative probability cutoff for token selection. Lower values mean
              sampling from a smaller, more top-weighted nucleus. Available for models
              provided by Google, LLM Engine, and OpenAI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        model_deployment_id: str,
        *,
        prompt: str,
        stream: bool,
        chat_template: str | NotGiven = NOT_GIVEN,
        chat_template_kwargs: object | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_request_parameters: ParameterBindingsParam | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse | AsyncStream[CompletionResponse]:
        """
        ### Description

        Interact with the LLM model using the specified model_deployment_id. The LLM
        model will generate a text completion based on the provided prompt.

        ```json
        {
          "prompt": "What is the capital of France?"
        }
        ```

        Args:
          stream: Flag indicating whether to stream the completion response

          chat_template: The chat template to use for the completion. Currently only supported for
              llmengine chat models.

          chat_template_kwargs: Additional keyword arguments for the chat template. Currently only supported for
              llmengine chat models.

          frequency_penalty: Penalize tokens based on how much they have already appeared in the text.
              Positive values encourage the model to generate new tokens and negative values
              encourage the model to repeat tokens. Available for models provided by LLM
              Engine and OpenAI.

          logprobs: Whether to return logprobs. Currently only supported for llmengine chat models.

          max_tokens: The maximum number of tokens to generate in the completion. The token count of
              your prompt plus max_tokens cannot exceed the model's context length. If not,
              specified, max_tokens will be determined based on the model used: | Model API
              family | Model API default | EGP applied default | | --- | --- | --- | | OpenAI
              Completions |
              [`16`](https://platform.openai.com/docs/api-reference/completions/create#max_tokens)
              | `context window - prompt size` | | OpenAI Chat Completions |
              [`context window - prompt size`](https://platform.openai.com/docs/api-reference/chat/create#max_tokens)
              | `context window - prompt size` | | LLM Engine |
              [`max_new_tokens`](https://github.com/scaleapi/launch-python-client/blob/207adced1c88c1c2907266fa9dd1f1ff3ec0ea5b/launch/client.py#L2910)
              parameter is required | `100` | | Anthropic Claude 2 |
              [`max_tokens_to_sample`](https://docs.anthropic.com/claude/reference/complete_post)
              parameter is required | `10000` |

          presence_penalty: Penalize tokens based on if they have already appeared in the text. Positive
              values encourage the model to generate new tokens and negative values encourage
              the model to repeat tokens. Available for models provided by LLM Engine and
              OpenAI.

          stop_sequences: List of up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          temperature: What sampling temperature to use, between [0, 2]. Higher values like 1.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. Setting temperature=0.0 will enable fully
              deterministic (greedy) sampling.NOTE: The temperature parameter range for some
              model is limited to [0, 1] if the given value is above the available range, it
              defaults to the max value.

          top_k: Sample from the k most likely next tokens at each step. Lower k focuses on
              higher probability tokens. Available for models provided by Google and LLM
              Engine.

          top_logprobs: Number of top logprobs to return. Currently only supported for llmengine chat
              models.

          top_p: The cumulative probability cutoff for token selection. Lower values mean
              sampling from a smaller, more top-weighted nucleus. Available for models
              provided by Google, LLM Engine, and OpenAI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["prompt"], ["prompt", "stream"])
    async def create(
        self,
        model_deployment_id: str,
        *,
        prompt: str,
        chat_template: str | NotGiven = NOT_GIVEN,
        chat_template_kwargs: object | NotGiven = NOT_GIVEN,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        model_request_parameters: ParameterBindingsParam | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionResponse | AsyncStream[CompletionResponse]:
        if not model_deployment_id:
            raise ValueError(
                f"Expected a non-empty value for `model_deployment_id` but received {model_deployment_id!r}"
            )
        return await self._post(
            f"/v4/models/{model_deployment_id}/completions",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "chat_template": chat_template,
                    "chat_template_kwargs": chat_template_kwargs,
                    "frequency_penalty": frequency_penalty,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "model_request_parameters": model_request_parameters,
                    "presence_penalty": presence_penalty,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionResponse,
            stream=stream or False,
            stream_cls=AsyncStream[CompletionResponse],
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
