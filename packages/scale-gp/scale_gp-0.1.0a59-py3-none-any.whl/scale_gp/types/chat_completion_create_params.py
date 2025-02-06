# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ChatCompletionCreateParamsBase",
    "Message",
    "MessageUserMessage",
    "MessageUserMessageContentUserMessageContentPart",
    "MessageUserMessageContentUserMessageContentPartTextUserMessageContentParts",
    "MessageUserMessageContentUserMessageContentPartImageURLUserMessageContentParts",
    "MessageUserMessageContentUserMessageContentPartImageURLUserMessageContentPartsImageURL",
    "MessageUserMessageContentUserMessageContentPartImageDataUserMessageContentParts",
    "MessageUserMessageContentUserMessageContentPartImageDataUserMessageContentPartsImageData",
    "MessageAssistantMessage",
    "MessageSystemMessage",
    "MemoryStrategy",
    "MemoryStrategyParams",
    "ModelParameters",
    "ChatCompletionCreateParamsNonStreaming",
    "ChatCompletionCreateParamsStreaming",
]


class ChatCompletionCreateParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The list of messages in the conversation.

    Expand each message type to see how it works and when to use it. Most
    conversations should begin with a single `user` message.
    """

    model: Required[
        Literal[
            "gpt-4",
            "gpt-4-0613",
            "gpt-4-32k",
            "gpt-4-32k-0613",
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4o-2024-08-06",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-16k-0613",
            "gemini-pro",
            "gemini-1.5-pro-001",
            "gemini-1.5-pro-002",
            "gemini-1.5-pro-preview-0409",
            "gemini-1.5-pro-preview-0514",
            "llama-2-7b-chat",
            "llama-2-13b-chat",
            "llama-2-70b-chat",
            "llama-3-8b-instruct",
            "llama-3-70b-instruct",
            "llama-3-1-8b-instruct",
            "llama-3-1-70b-instruct",
            "llama-3-2-1b-instruct",
            "llama-3-2-3b-instruct",
            "Meta-Llama-3-8B-Instruct-RMU",
            "Meta-Llama-3-8B-Instruct-RR",
            "Meta-Llama-3-8B-Instruct-DERTA",
            "Meta-Llama-3-8B-Instruct-LAT",
            "mixtral-8x7b-instruct",
            "mixtral-8x22b-instruct",
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
            "claude-3-5-sonnet-20240620",
            "claude-3-5-sonnet-20241022",
            "mistral-large-latest",
            "phi-3-mini-4k-instruct",
            "phi-3-cat-merged",
            "zephyr-cat-merged",
            "dolphin-2.9-llama3-8b",
            "dolphin-2.9-llama3-70b",
            "llama3-1-405b-instruct-v1",
        ]
    ]
    """The ID of the model to use for chat completions.

    We only support the models listed here so far.
    """

    account_id: str
    """The account ID to use for usage tracking. This will be gradually enforced."""

    chat_template: str
    """Currently only supported for LLM-Engine models.

    A Jinja template string that defines how the chat completion API formats the
    string prompt. For Llama models, the template must take in at most a `messages`
    object, `bos_token` string, and `eos_token` string. The `messages` object is a
    list of dictionaries, each with keys `role` and `content`. For Mixtral models,
    the template must take in at most a `messages` object and `eos_token` string.
    The `messages` object looks identical to the Llama model's `messages` object,
    but the template can assume the `role` key takes on the values `user` or
    `assistant`, or `system` for the first message. The chat template either needs
    to handle this system message (which gets set via the `instructions` field or by
    the messages), or the `instructions` field must be set to `null` and the
    `messages` object must not contain any system messages.See the default chat
    template present in the Llama and Mixtral tokenizers for examples.
    """

    instructions: str
    """The initial instructions to provide to the chat completion model.

    Use this to guide the model to act in more specific ways. For example, if you
    have specific rules you want to restrict the model to follow you can specify
    them here.

    Good prompt engineering is crucial to getting performant results from the model.
    If you are having trouble getting the model to perform well, try writing more
    specific instructions here before trying more expensive techniques such as
    swapping in other models or finetuning the underlying LLM.
    """

    memory_strategy: MemoryStrategy
    """The memory strategy to use for the agent.

    A memory strategy is a way to prevent the underlying LLM's context limit from
    being exceeded. Each memory strategy uses a different technique to condense the
    input message list into a smaller payload for the underlying LLM.

    We only support the Last K memory strategy right now, but will be adding new
    strategies soon.
    """

    model_parameters: ModelParameters
    """
    Configuration parameters for the chat completion model, such as temperature,
    max_tokens, and stop_sequences.

    If not specified, the default value are:

    - temperature: 0.2
    - max_tokens: None (limited by the model's max tokens)
    - stop_sequences: None
    """


class MessageUserMessageContentUserMessageContentPartTextUserMessageContentParts(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MessageUserMessageContentUserMessageContentPartImageURLUserMessageContentPartsImageURL(TypedDict, total=False):
    url: Required[str]
    """The URL of the image. Note: only OpenAI supports this."""

    detail: Literal["low", "high", "auto"]
    """Only used for OpenAI. Corresponds to OpenAI's image detail parameter."""


class MessageUserMessageContentUserMessageContentPartImageURLUserMessageContentParts(TypedDict, total=False):
    image_url: Required[MessageUserMessageContentUserMessageContentPartImageURLUserMessageContentPartsImageURL]
    """Specifies the image URL and level of detail. Only supported by OpenAI models"""

    type: Literal["image_url"]


class MessageUserMessageContentUserMessageContentPartImageDataUserMessageContentPartsImageData(TypedDict, total=False):
    data: Required[str]
    """The base64-encoded image data."""

    media_type: Required[str]
    """The media/mime type of the image data.

    For example, 'image/png'. Check providers' documentation for supported media
    types.
    """

    detail: Literal["low", "high", "auto"]
    """Only used for OpenAI. Corresponds to OpenAI's image detail parameter."""

    type: Literal["base64"]
    """The type of the image data. Only base64 is supported."""


class MessageUserMessageContentUserMessageContentPartImageDataUserMessageContentParts(TypedDict, total=False):
    image_data: Required[MessageUserMessageContentUserMessageContentPartImageDataUserMessageContentPartsImageData]
    """Specifies inline image data"""

    type: Literal["image_data"]


MessageUserMessageContentUserMessageContentPart: TypeAlias = Union[
    MessageUserMessageContentUserMessageContentPartTextUserMessageContentParts,
    MessageUserMessageContentUserMessageContentPartImageURLUserMessageContentParts,
    MessageUserMessageContentUserMessageContentPartImageDataUserMessageContentParts,
]


class MessageUserMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageUserMessageContentUserMessageContentPart]]]
    """Input from the user.

    Can either be text or a list of content parts. Not all models support image
    content parts, or multiple parts.
    """

    role: Literal["user"]
    """The role of the message. Must be set to 'user'.

    A user message is a message from the user to the AI. This should be the message
    used to send end user input to the AI.
    """


class MessageAssistantMessage(TypedDict, total=False):
    content: Required[str]
    """Text response from the assistant"""

    role: Literal["assistant"]
    """The role of the message. Must be set to 'assistant'.

    An assistant message is a message from the AI to the client. It is different
    from an agent message in that it cannot contain a tool request. It is simply a
    direct response from the AI to the client.
    """


class MessageSystemMessage(TypedDict, total=False):
    content: Required[str]
    """Text input from the system."""

    role: Literal["system"]
    """The role of the message. Must be set to 'system'.

    A system message is different from other messages in that it does not originate
    from a party engaged in a user/AI conversation. Instead, it is a message that is
    injected by either the application or system to guide the conversation. For
    example, a system message may be used as initial instructions for an AI entity
    or to tell the AI that it did not do something correctly.
    """


Message: TypeAlias = Union[MessageUserMessage, MessageAssistantMessage, MessageSystemMessage]


class MemoryStrategyParams(TypedDict, total=False):
    k: Required[int]
    """The maximum number of previous messages to remember."""


class MemoryStrategy(TypedDict, total=False):
    params: Required[MemoryStrategyParams]
    """Configuration parameters for the memory strategy."""

    name: Literal["last_k"]
    """Name of the memory strategy. Must be `last_k`.

    This strategy truncates the message history to the last `k` messages. It is the
    simplest way to prevent the model's context limit from being exceeded. However,
    this strategy only allows the model to have short term memory. For longer term
    memory, please use one of the other strategies.
    """


class ModelParameters(TypedDict, total=False):
    frequency_penalty: float
    """Penalize tokens based on how much they have already appeared in the text.

    Positive values encourage the model to generate new tokens and negative values
    encourage the model to repeat tokens. Available for models from LLM Engine, and
    OpenAI
    """

    max_tokens: int
    """The maximum number of tokens to generate in the completion.

    The token count of your prompt plus max_tokens cannot exceed the model's context
    length. If not, specified, max_tokens will be determined based on the model
    used: | Model API family | Model API default | EGP applied default | | --- | ---
    | --- | | OpenAI Completions |
    [`16`](https://platform.openai.com/docs/api-reference/completions/create#max_tokens)
    | `context window - prompt size` | | OpenAI Chat Completions |
    [`context window - prompt size`](https://platform.openai.com/docs/api-reference/chat/create#max_tokens)
    | `context window - prompt size` | | LLM Engine |
    [`max_new_tokens`](https://github.com/scaleapi/launch-python-client/blob/207adced1c88c1c2907266fa9dd1f1ff3ec0ea5b/launch/client.py#L2910)
    parameter is required | `100` | | Anthropic Claude 2 |
    [`max_tokens_to_sample`](https://docs.anthropic.com/claude/reference/complete_post)
    parameter is required | `10000` |
    """

    presence_penalty: float
    """Penalize tokens based on if they have already appeared in the text.

    Positive values encourage the model to generate new tokens and negative values
    encourage the model to repeat tokens. Available for models from LLM Engine, and
    OpenAI.
    """

    stop_sequences: List[str]
    """List of up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    temperature: float
    """What sampling temperature to use, between [0, 1].

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. Setting temperature=0.0 will
    enable fully deterministic (greedy) sampling.
    """

    top_k: Annotated[int, PropertyInfo(alias="topK")]
    """Sample from the k most likely next tokens at each step.

    Lower k focuses on higher probability tokens. Available for models from
    Anthropic, Google, and LLM Engine.
    """

    top_p: Annotated[float, PropertyInfo(alias="topP")]
    """The cumulative probability cutoff for token selection.

    Lower values mean sampling from a smaller, more top-weighted nucleus. Available
    for models from Anthropic, Google, Mistral, LLM Engine, and OpenAI.
    """


class ChatCompletionCreateParamsNonStreaming(ChatCompletionCreateParamsBase, total=False):
    stream: Literal[False]
    """Whether or not to stream the response.

    Setting this to True will stream the completion in real-time.
    """


class ChatCompletionCreateParamsStreaming(ChatCompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """Whether or not to stream the response.

    Setting this to True will stream the completion in real-time.
    """


ChatCompletionCreateParams = Union[ChatCompletionCreateParamsNonStreaming, ChatCompletionCreateParamsStreaming]
