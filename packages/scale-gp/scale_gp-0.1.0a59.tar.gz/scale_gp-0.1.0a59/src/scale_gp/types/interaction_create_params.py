# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["InteractionCreateParams", "Input", "Output", "OutputContext", "GuardrailResult", "TraceSpan"]


class InteractionCreateParams(TypedDict, total=False):
    application_variant_id: Required[str]
    """Identifier for the application variant that performed this interaction."""

    input: Required[Input]
    """The input data for the interaction."""

    output: Required[Output]
    """The output data from the interaction."""

    start_timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp marking the start of the interaction."""

    duration_ms: int
    """Duration of the interaction in milliseconds."""

    guardrail_results: Iterable[GuardrailResult]
    """Results of the guardrails executed on the input"""

    operation_metadata: object
    """
    Optional metadata related to the operation, including custom or predefined keys.
    """

    operation_status: Literal["SUCCESS", "ERROR"]
    """The outcome status of the interaction."""

    thread_id: str
    """
    Optional UUID identifying the conversation thread associated with the
    interaction.The interaction will be associated with the thread if the id
    represents an existing thread.If the thread with the specified id is not found,
    a new thread will be created.
    """

    trace_spans: Iterable[TraceSpan]
    """
    List of trace spans associated with the interaction.These spans provide insight
    into the individual steps taken by nodes involved in generating the output.
    """


class InputTyped(TypedDict, total=False):
    query: Required[str]
    """The query or input text for the interaction."""


Input: TypeAlias = Union[InputTyped, Dict[str, object]]


class OutputContextTyped(TypedDict, total=False):
    text: Required[str]
    """The text of the context entry."""

    score: float
    """The score of the context entry."""


OutputContext: TypeAlias = Union[OutputContextTyped, Dict[str, object]]


class OutputTyped(TypedDict, total=False):
    response: Required[str]
    """The response or output text of the interaction."""

    context: Iterable[OutputContext]
    """Optional context information provided with the response."""


Output: TypeAlias = Union[OutputTyped, Dict[str, object]]


class GuardrailResult(TypedDict, total=False):
    guardrail_id: Required[str]

    policy_id: Required[str]

    score: Required[float]

    severity: Required[Literal["low", "high"]]

    triggered: Required[bool]

    description: str

    result_metadata: object


class TraceSpan(TypedDict, total=False):
    node_id: Required[str]
    """Identifier for the node that emitted this trace span."""

    operation_type: Required[Literal["COMPLETION", "RERANKING", "RETRIEVAL", "CUSTOM"]]
    """Type of the operation, e.g., RERANKING."""

    start_timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The start time of the step."""

    duration_ms: int
    """The duration of the operation step in milliseconds."""

    operation_input: object
    """The JSON representation of the input that this step received."""

    operation_metadata: object
    """The JSON representation of the metadata insights emitted during execution.

    This can differ based on different types of operations.
    """

    operation_output: object
    """The JSON representation of the output that this step emitted."""

    operation_status: Literal["SUCCESS", "ERROR"]
    """The outcome of the operation performed by this node."""
