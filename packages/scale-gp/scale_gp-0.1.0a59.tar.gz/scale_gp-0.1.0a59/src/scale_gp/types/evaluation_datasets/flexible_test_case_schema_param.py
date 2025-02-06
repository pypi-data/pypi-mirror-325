# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .flexible_chunk_param import FlexibleChunkParam
from .flexible_message_param import FlexibleMessageParam
from ..shared_params.chunk_extra_info_schema import ChunkExtraInfoSchema
from ..shared_params.string_extra_info_schema import StringExtraInfoSchema

__all__ = [
    "FlexibleTestCaseSchemaParam",
    "InputAdditionalObjectInputAdditionalObjectItem",
    "InputAdditionalObjectInputAdditionalObjectItemExternalFile",
    "InputAdditionalObjectInputAdditionalObjectItemInternalFile",
    "ExpectedExtraInfo",
    "ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItem",
    "ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemExternalFile",
    "ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemInternalFile",
]


class InputAdditionalObjectInputAdditionalObjectItemExternalFile(TypedDict, total=False):
    file_type: Required[Literal["image"]]

    uri: Required[str]


class InputAdditionalObjectInputAdditionalObjectItemInternalFile(TypedDict, total=False):
    file_id: Required[str]

    file_type: Required[Literal["image"]]


InputAdditionalObjectInputAdditionalObjectItem: TypeAlias = Union[
    str,
    float,
    Iterable[FlexibleChunkParam],
    Iterable[FlexibleMessageParam],
    Iterable[object],
    InputAdditionalObjectInputAdditionalObjectItemExternalFile,
    InputAdditionalObjectInputAdditionalObjectItemInternalFile,
    object,
]

ExpectedExtraInfo: TypeAlias = Union[ChunkExtraInfoSchema, StringExtraInfoSchema]


class ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemExternalFile(TypedDict, total=False):
    file_type: Required[Literal["image"]]

    uri: Required[str]


class ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemInternalFile(TypedDict, total=False):
    file_id: Required[str]

    file_type: Required[Literal["image"]]


ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItem: TypeAlias = Union[
    str,
    float,
    Iterable[FlexibleChunkParam],
    Iterable[FlexibleMessageParam],
    Iterable[object],
    ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemExternalFile,
    ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemInternalFile,
    object,
]


class FlexibleTestCaseSchemaParam(TypedDict, total=False):
    input: Required[Union[str, Dict[str, InputAdditionalObjectInputAdditionalObjectItem]]]

    expected_extra_info: ExpectedExtraInfo

    expected_output: Union[str, Dict[str, ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItem]]
