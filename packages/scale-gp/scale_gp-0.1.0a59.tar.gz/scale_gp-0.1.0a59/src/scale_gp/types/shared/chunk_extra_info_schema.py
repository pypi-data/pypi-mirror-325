# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChunkExtraInfoSchema", "Chunk"]


class Chunk(BaseModel):
    text: str

    metadata: Optional[object] = None


class ChunkExtraInfoSchema(BaseModel):
    chunks: List[Chunk]

    schema_type: Optional[Literal["CHUNKS"]] = None
