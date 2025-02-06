# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "InteractionCreateResponse",
    "Input",
    "Output",
    "OutputContext",
    "GuardrailResult",
    "GuardrailResultGuardrail",
    "GuardrailResultPolicy",
    "TraceSpan",
]


class Input(BaseModel):
    query: str
    """The query or input text for the interaction."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class OutputContext(BaseModel):
    text: str
    """The text of the context entry."""

    score: Optional[float] = None
    """The score of the context entry."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Output(BaseModel):
    response: str
    """The response or output text of the interaction."""

    context: Optional[List[OutputContext]] = None
    """Optional context information provided with the response."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class GuardrailResultGuardrail(BaseModel):
    id: str

    account_id: str

    check_type: Literal["input", "output"]

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    description: Optional[str] = None

    guardrail_metadata: Optional[object] = None

    is_archived: Optional[bool] = None


class GuardrailResultPolicy(BaseModel):
    id: str

    category: str

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    guardrail_id: str

    unsafe_threshold: float

    description: Optional[str] = None

    guardrail_policy_metadata: Optional[object] = None


class GuardrailResult(BaseModel):
    id: str

    application_interaction_id: str

    application_spec_id: str

    application_variant_id: str

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    guardrail: GuardrailResultGuardrail

    guardrail_id: str

    policy: GuardrailResultPolicy

    policy_id: str

    score: float

    severity: Literal["low", "high"]

    triggered: bool

    description: Optional[str] = None

    result_metadata: Optional[object] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class TraceSpan(BaseModel):
    id: str
    """Unique identifier for the trace span."""

    application_interaction_id: str
    """The ID of the application interaction this trace span belongs to."""

    node_id: str
    """Identifier for the node that emitted this trace span."""

    operation_type: Literal["COMPLETION", "RERANKING", "RETRIEVAL", "CUSTOM"]
    """Type of the operation, e.g., RERANKING."""

    start_timestamp: datetime
    """The start time of the step."""

    duration_ms: Optional[int] = None
    """The duration of the operation step in milliseconds."""

    operation_input: Optional[object] = None
    """The JSON representation of the input that this step received."""

    operation_metadata: Optional[object] = None
    """The JSON representation of the metadata insights emitted during execution.

    This can differ based on different types of operations.
    """

    operation_output: Optional[object] = None
    """The JSON representation of the output that this step emitted."""

    operation_status: Optional[Literal["SUCCESS", "ERROR"]] = None
    """The outcome of the operation performed by this node."""


class InteractionCreateResponse(BaseModel):
    id: str
    """Unique identifier for the interaction."""

    application_variant_id: str
    """Identifier for the application variant that performed this interaction."""

    input: Input
    """The input data for the interaction."""

    output: Output
    """The output data from the interaction."""

    start_timestamp: datetime
    """Timestamp marking the start of the interaction."""

    duration_ms: Optional[int] = None
    """Duration of the interaction in milliseconds."""

    guardrail_results: Optional[List[GuardrailResult]] = None
    """Results of the guardrails executed on the input"""

    operation_metadata: Optional[object] = None
    """
    Optional metadata related to the operation, including custom or predefined keys.
    """

    operation_status: Optional[Literal["SUCCESS", "ERROR"]] = None
    """The outcome status of the interaction."""

    thread_id: Optional[str] = None
    """
    Optional UUID identifying the conversation thread associated with the
    interaction.The interaction will be associated with the thread if the id
    represents an existing thread.If the thread with the specified id is not found,
    a new thread will be created.
    """

    trace_spans: Optional[List[TraceSpan]] = None
    """List of trace span entities associated with the interaction."""
