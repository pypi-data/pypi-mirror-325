# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ChatCompletionsResponse",
    "ChatCompletion",
    "ChatCompletionMessage",
    "ChatCompletionMessageUserMessage",
    "ChatCompletionMessageUserMessageContentUserMessageContentPart",
    "ChatCompletionMessageUserMessageContentUserMessageContentPartTextUserMessageContentParts",
    "ChatCompletionMessageUserMessageContentUserMessageContentPartImageURLUserMessageContentParts",
    "ChatCompletionMessageUserMessageContentUserMessageContentPartImageURLUserMessageContentPartsImageURL",
    "ChatCompletionMessageUserMessageContentUserMessageContentPartImageDataUserMessageContentParts",
    "ChatCompletionMessageUserMessageContentUserMessageContentPartImageDataUserMessageContentPartsImageData",
    "ChatCompletionMessageAssistantMessage",
    "ChatCompletionMessageSystemMessage",
    "TokenUsage",
]


class ChatCompletionMessageUserMessageContentUserMessageContentPartTextUserMessageContentParts(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChatCompletionMessageUserMessageContentUserMessageContentPartImageURLUserMessageContentPartsImageURL(BaseModel):
    url: str
    """The URL of the image. Note: only OpenAI supports this."""

    detail: Optional[Literal["low", "high", "auto"]] = None
    """Only used for OpenAI. Corresponds to OpenAI's image detail parameter."""


class ChatCompletionMessageUserMessageContentUserMessageContentPartImageURLUserMessageContentParts(BaseModel):
    image_url: ChatCompletionMessageUserMessageContentUserMessageContentPartImageURLUserMessageContentPartsImageURL
    """Specifies the image URL and level of detail. Only supported by OpenAI models"""

    type: Optional[Literal["image_url"]] = None


class ChatCompletionMessageUserMessageContentUserMessageContentPartImageDataUserMessageContentPartsImageData(BaseModel):
    data: str
    """The base64-encoded image data."""

    media_type: str
    """The media/mime type of the image data.

    For example, 'image/png'. Check providers' documentation for supported media
    types.
    """

    detail: Optional[Literal["low", "high", "auto"]] = None
    """Only used for OpenAI. Corresponds to OpenAI's image detail parameter."""

    type: Optional[Literal["base64"]] = None
    """The type of the image data. Only base64 is supported."""


class ChatCompletionMessageUserMessageContentUserMessageContentPartImageDataUserMessageContentParts(BaseModel):
    image_data: ChatCompletionMessageUserMessageContentUserMessageContentPartImageDataUserMessageContentPartsImageData
    """Specifies inline image data"""

    type: Optional[Literal["image_data"]] = None


ChatCompletionMessageUserMessageContentUserMessageContentPart: TypeAlias = Annotated[
    Union[
        ChatCompletionMessageUserMessageContentUserMessageContentPartTextUserMessageContentParts,
        ChatCompletionMessageUserMessageContentUserMessageContentPartImageURLUserMessageContentParts,
        ChatCompletionMessageUserMessageContentUserMessageContentPartImageDataUserMessageContentParts,
    ],
    PropertyInfo(discriminator="type"),
]


class ChatCompletionMessageUserMessage(BaseModel):
    content: Union[str, List[ChatCompletionMessageUserMessageContentUserMessageContentPart]]
    """Input from the user.

    Can either be text or a list of content parts. Not all models support image
    content parts, or multiple parts.
    """

    role: Optional[Literal["user"]] = None
    """The role of the message. Must be set to 'user'.

    A user message is a message from the user to the AI. This should be the message
    used to send end user input to the AI.
    """


class ChatCompletionMessageAssistantMessage(BaseModel):
    content: str
    """Text response from the assistant"""

    role: Optional[Literal["assistant"]] = None
    """The role of the message. Must be set to 'assistant'.

    An assistant message is a message from the AI to the client. It is different
    from an agent message in that it cannot contain a tool request. It is simply a
    direct response from the AI to the client.
    """


class ChatCompletionMessageSystemMessage(BaseModel):
    content: str
    """Text input from the system."""

    role: Optional[Literal["system"]] = None
    """The role of the message. Must be set to 'system'.

    A system message is different from other messages in that it does not originate
    from a party engaged in a user/AI conversation. Instead, it is a message that is
    injected by either the application or system to guide the conversation. For
    example, a system message may be used as initial instructions for an AI entity
    or to tell the AI that it did not do something correctly.
    """


ChatCompletionMessage: TypeAlias = Annotated[
    Union[ChatCompletionMessageUserMessage, ChatCompletionMessageAssistantMessage, ChatCompletionMessageSystemMessage],
    PropertyInfo(discriminator="role"),
]


class ChatCompletion(BaseModel):
    message: ChatCompletionMessage

    finish_reason: Optional[str] = None


class TokenUsage(BaseModel):
    total: int
    """Total number of tokens in both the prompt and the completion."""

    completion: Optional[int] = None
    """Number of tokens in the completion."""

    prompt: Optional[int] = None
    """Number of tokens in the prompt."""


class ChatCompletionsResponse(BaseModel):
    chat_completion: ChatCompletion

    token_usage: Optional[TokenUsage] = None
