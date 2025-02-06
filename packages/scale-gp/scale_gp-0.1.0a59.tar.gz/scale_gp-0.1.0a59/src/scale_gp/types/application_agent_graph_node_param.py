# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ApplicationAgentGraphNodeParam", "Edge"]


class Edge(TypedDict, total=False):
    from_node: Required[str]

    to_node: Required[str]


class ApplicationAgentGraphNodeParam(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    type: Required[str]

    config: object

    edges: Iterable[Edge]

    nodes: Iterable["ApplicationAgentGraphNodeParam"]

    operation_type: Literal[
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
