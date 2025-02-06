# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.chunk_extra_info_schema import ChunkExtraInfoSchema
from .shared_params.string_extra_info_schema import StringExtraInfoSchema
from .evaluation_datasets.flexible_chunk_param import FlexibleChunkParam
from .evaluation_datasets.flexible_message_param import FlexibleMessageParam

__all__ = [
    "ResultSchemaFlexibleParam",
    "GenerationOutputAdditionalObjectGenerationOutputAdditionalObjectItem",
    "GenerationOutputAdditionalObjectGenerationOutputAdditionalObjectItemExternalFile",
    "GenerationOutputAdditionalObjectGenerationOutputAdditionalObjectItemInternalFile",
    "GenerationExtraInfo",
]


class GenerationOutputAdditionalObjectGenerationOutputAdditionalObjectItemExternalFile(TypedDict, total=False):
    file_type: Required[Literal["image"]]

    uri: Required[str]


class GenerationOutputAdditionalObjectGenerationOutputAdditionalObjectItemInternalFile(TypedDict, total=False):
    file_id: Required[str]

    file_type: Required[Literal["image"]]


GenerationOutputAdditionalObjectGenerationOutputAdditionalObjectItem: TypeAlias = Union[
    str,
    float,
    Iterable[FlexibleChunkParam],
    Iterable[FlexibleMessageParam],
    Iterable[object],
    GenerationOutputAdditionalObjectGenerationOutputAdditionalObjectItemExternalFile,
    GenerationOutputAdditionalObjectGenerationOutputAdditionalObjectItemInternalFile,
    object,
]

GenerationExtraInfo: TypeAlias = Union[ChunkExtraInfoSchema, StringExtraInfoSchema]


class ResultSchemaFlexibleParam(TypedDict, total=False):
    generation_output: Required[
        Union[str, Dict[str, GenerationOutputAdditionalObjectGenerationOutputAdditionalObjectItem]]
    ]

    generation_extra_info: GenerationExtraInfo
