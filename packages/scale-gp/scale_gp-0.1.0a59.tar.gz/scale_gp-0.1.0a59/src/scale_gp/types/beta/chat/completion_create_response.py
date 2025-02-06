# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from .chat_completion_chunk import ChatCompletionChunk

__all__ = [
    "CompletionCreateResponse",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletion",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoice",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessage",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageAudio",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageFunctionCall",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageToolCall",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageToolCallFunction",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobs",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsContent",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsContentTopLogprob",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsRefusal",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsRefusalTopLogprob",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionUsage",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionUsageCompletionTokensDetails",
    "EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionUsagePromptTokensDetails",
]


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageAudio(BaseModel):
    id: str

    data: str

    expires_at: int

    transcript: str

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageFunctionCall(BaseModel):
    arguments: str

    name: str

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageToolCallFunction(BaseModel):
    arguments: str

    name: str

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageToolCall(BaseModel):
    id: str

    function: EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageToolCallFunction

    type: Literal["function"]

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessage(BaseModel):
    role: Literal["assistant"]

    audio: Optional[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageAudio] = None

    content: Optional[str] = None

    function_call: Optional[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageFunctionCall] = None

    refusal: Optional[str] = None

    tool_calls: Optional[List[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessageToolCall]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobs(BaseModel):
    content: Optional[List[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsContent]] = None

    refusal: Optional[List[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobsRefusal]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoice(BaseModel):
    finish_reason: Literal["stop", "length", "tool_calls", "content_filter", "function_call"]

    index: int

    message: EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceMessage

    logprobs: Optional[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoiceLogprobs] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionUsageCompletionTokensDetails(BaseModel):
    accepted_prediction_tokens: Optional[int] = None

    audio_tokens: Optional[int] = None

    reasoning_tokens: Optional[int] = None

    rejected_prediction_tokens: Optional[int] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionUsagePromptTokensDetails(BaseModel):
    audio_tokens: Optional[int] = None

    cached_tokens: Optional[int] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionUsage(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int

    completion_tokens_details: Optional[
        EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionUsageCompletionTokensDetails
    ] = None

    prompt_tokens_details: Optional[
        EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionUsagePromptTokensDetails
    ] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EgpAPIBackendServerAPIModelsInferenceModelsChatCompletion(BaseModel):
    id: str

    choices: List[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionChoice]

    created: int

    model: str

    object: Optional[Literal["chat.completion"]] = None

    service_tier: Optional[Literal["scale", "default"]] = None

    system_fingerprint: Optional[str] = None

    usage: Optional[EgpAPIBackendServerAPIModelsInferenceModelsChatCompletionUsage] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...


CompletionCreateResponse: TypeAlias = Union[
    EgpAPIBackendServerAPIModelsInferenceModelsChatCompletion, ChatCompletionChunk
]
