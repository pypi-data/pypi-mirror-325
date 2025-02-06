# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .flexible_chunk import FlexibleChunk
from .flexible_message import FlexibleMessage
from ..shared.chunk_extra_info_schema import ChunkExtraInfoSchema
from ..shared.string_extra_info_schema import StringExtraInfoSchema

__all__ = [
    "FlexibleTestCaseSchema",
    "InputAdditionalObjectInputAdditionalObjectItem",
    "InputAdditionalObjectInputAdditionalObjectItemExternalFile",
    "InputAdditionalObjectInputAdditionalObjectItemInternalFile",
    "ExpectedExtraInfo",
    "ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItem",
    "ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemExternalFile",
    "ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemInternalFile",
]


class InputAdditionalObjectInputAdditionalObjectItemExternalFile(BaseModel):
    file_type: Literal["image"]

    uri: str


class InputAdditionalObjectInputAdditionalObjectItemInternalFile(BaseModel):
    file_id: str

    file_type: Literal["image"]


InputAdditionalObjectInputAdditionalObjectItem: TypeAlias = Union[
    str,
    float,
    List[FlexibleChunk],
    List[FlexibleMessage],
    List[object],
    InputAdditionalObjectInputAdditionalObjectItemExternalFile,
    InputAdditionalObjectInputAdditionalObjectItemInternalFile,
    object,
]

ExpectedExtraInfo: TypeAlias = Annotated[
    Union[ChunkExtraInfoSchema, StringExtraInfoSchema], PropertyInfo(discriminator="schema_type")
]


class ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemExternalFile(BaseModel):
    file_type: Literal["image"]

    uri: str


class ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemInternalFile(BaseModel):
    file_id: str

    file_type: Literal["image"]


ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItem: TypeAlias = Union[
    str,
    float,
    List[FlexibleChunk],
    List[FlexibleMessage],
    List[object],
    ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemExternalFile,
    ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItemInternalFile,
    object,
]


class FlexibleTestCaseSchema(BaseModel):
    input: Union[str, Dict[str, InputAdditionalObjectInputAdditionalObjectItem]]

    expected_extra_info: Optional[ExpectedExtraInfo] = None

    expected_output: Union[str, Dict[str, ExpectedOutputAdditionalObjectExpectedOutputAdditionalObjectItem], None] = (
        None
    )
