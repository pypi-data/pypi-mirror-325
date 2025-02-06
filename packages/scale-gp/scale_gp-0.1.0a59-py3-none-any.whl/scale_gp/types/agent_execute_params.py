# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AgentExecuteParams",
    "Message",
    "MessageUserMessage",
    "MessageUserMessageContentUserMessageContentPart",
    "MessageUserMessageContentUserMessageContentPartTextUserMessageContentParts",
    "MessageUserMessageContentUserMessageContentPartImageURLUserMessageContentParts",
    "MessageUserMessageContentUserMessageContentPartImageURLUserMessageContentPartsImageURL",
    "MessageUserMessageContentUserMessageContentPartImageDataUserMessageContentParts",
    "MessageUserMessageContentUserMessageContentPartImageDataUserMessageContentPartsImageData",
    "MessageToolMessage",
    "MessageAgentMessage",
    "MessageAgentMessageToolRequest",
    "MessageSystemMessage",
    "Tool",
    "ToolArguments",
    "ToolArgumentsProperties",
    "MemoryStrategy",
    "MemoryStrategyParams",
    "ModelParameters",
]


class AgentExecuteParams(TypedDict, total=False):
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
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-16k-0613",
            "claude-instant-1",
            "claude-instant-1.1",
            "claude-2",
            "claude-2.0",
        ]
    ]
    """The ID of the model to use for the agent.

    We only support the models listed here so far.
    """

    tools: Required[Iterable[Tool]]
    """The list of specs of tools that the agent can use.

    Each spec must contain a `name` key set to the name of the tool, a `description`
    key set to the description of the tool, and an `arguments` key set to a JSON
    Schema compliant object describing the tool arguments.

    The name and description of each tool is used by the agent to decide when to use
    certain tools. Because some queries are complex and may require multiple tools
    to complete, it is important to make these descriptions as informative as
    possible. If a tool is not being chosen when it should, it is common practice to
    tune the description of the tool to make it more apparent to the agent when the
    tool can be used effectively.
    """

    instructions: str
    """The initial instructions to provide to the agent.

    Use this to guide the agent to act in more specific ways. For example, if you
    have specific rules you want to restrict the agent to follow you can specify
    them here. For example, if I want the agent to always use certain tools before
    others, I can write that rule in these instructions.

    Good prompt engineering is crucial to getting performant results from the agent.
    If you are having trouble getting the agent to perform well, try writing more
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
    Configuration parameters for the agent model, such as temperature, max_tokens,
    and stop_sequences.

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


class MessageToolMessage(TypedDict, total=False):
    content: Required[str]
    """Text output from the tool"""

    name: Required[str]
    """Name of the tool"""

    role: Literal["tool"]
    """The role of the message. Must be set to 'tool'.

    A tool message is a message the client application uses to send tool output to
    the AI. It should contain the name of the tool and the output from the tool
    encoded as text.
    """


class MessageAgentMessageToolRequest(TypedDict, total=False):
    arguments: Required[str]
    """Arguments to pass to the tool.

    The format must be a JSON Schema-compliant object serialized into a string.
    """

    name: Required[str]
    """Name of the tool that the AI wants the client to use."""


class MessageAgentMessage(TypedDict, total=False):
    content: str
    """Text output of the agent if no more tools are needed."""

    role: Literal["agent"]
    """The role of the message. Must be set to 'agent'.

    An agent message is a message generated by an AI agent. It is different than an
    assistant message in that it can either contain a direct content output or a
    tool request that the client application must handle.
    """

    tool_request: MessageAgentMessageToolRequest
    """The tool request if the agent needs more information."""


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


Message: TypeAlias = Union[MessageUserMessage, MessageToolMessage, MessageAgentMessage, MessageSystemMessage]


class ToolArgumentsProperties(TypedDict, total=False):
    description: Required[str]
    """Description of what the argument is used for.

    This description is used to help the Agent generate sensible arguments for the
    tool. It is very important that this description is succinct, clear, and
    accurate.
    """

    type: Required[Literal["string", "number", "integer", "boolean", "object", "array", "null"]]
    """The argument's type.

    The type is used to help the Agent generate valid arguments for the tool.

    For more information about types, see:
    https://json-schema.org/understanding-json-schema/reference/type.html#type-specific-keywords
    """

    default: str
    """A default value for the argument if unspecified."""

    examples: List[str]
    """Example values demonstrating how the argument should look.

    This can be used to help the agent understand what a valid argument should look
    like.
    """


class ToolArguments(TypedDict, total=False):
    type: Required[Literal["object"]]
    """Type of argument. Currently only "object" is supported"""

    properties: Dict[str, ToolArgumentsProperties]
    """
    An object where each key is the name of a keyword argument and each value is a
    schema used to validate that property. Each schema must have a type and
    description, but can also have a default value and examples.

    For more information on how to define a valid property, visit
    https://json-schema.org/understanding-json-schema/reference/object.html
    """


class Tool(TypedDict, total=False):
    arguments: Required[ToolArguments]
    """An JSON Schema-compliant schema for the tool arguments.

    To describe a function that accepts no parameters, provide the value
    `{"type": ""object", "properties": {}}`.

    For more information on how to define a valid JSON Schema object, visit
    https://json-schema.org/understanding-json-schema/reference/object.html
    """

    description: Required[str]
    """Description of the tool.

    Because some queries are complex and may require multiple tools to complete, it
    is important to make these descriptions as informative as possible. If a tool is
    not being chosen when it should, it is common practice to tune the description
    of the tool to make it more apparent to the agent when the tool can be used
    effectively.
    """

    name: Required[str]
    """Name of the tool.

    A tool is a function that the _client application_ has at its disposal. The tool
    name is the name the client wishes the Agent to use to refer to this function
    when it decides if it wants the user to use the tool or not. Itmust be unique
    amongst the set of tools provided in a single API call.
    """


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
