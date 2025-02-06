# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["ApplicationAgentGraphNode", "Edge"]


class Edge(BaseModel):
    from_node: str

    to_node: str


class ApplicationAgentGraphNode(BaseModel):
    id: str

    name: str

    type: str

    config: Optional[object] = None

    edges: Optional[List[Edge]] = None

    nodes: Optional[List["ApplicationAgentGraphNode"]] = None

    operation_type: Optional[
        Literal[
            "TEXT_INPUT",
            "TEXT_OUTPUT",
            "COMPLETION_INPUT",
            "COMPLETION",
            "KB_RETRIEVAL",
            "KB_INPUT",
            "RERANKING",
            "EXTERNAL_ENDPOINT",
            "PROMPT_ENGINEERING",
            "DOCUMENT_INPUT",
            "MAP_REDUCE",
            "DOCUMENT_SEARCH",
            "DOCUMENT_PROMPT",
            "CUSTOM",
            "INPUT_GUARDRAIL",
            "OUTPUT_GUARDRAIL",
            "CODE_EXECUTION",
            "DATA_MANIPULATION",
            "EVALUATION",
            "FILE_RETRIEVAL",
        ]
    ] = None


if PYDANTIC_V2:
    ApplicationAgentGraphNode.model_rebuild()
    Edge.model_rebuild()
else:
    ApplicationAgentGraphNode.update_forward_refs()  # type: ignore
    Edge.update_forward_refs()  # type: ignore
