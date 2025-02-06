# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .application_configuration import ApplicationConfiguration

__all__ = [
    "ApplicationVariantCreateResponse",
    "ApplicationVariantV0Response",
    "ApplicationVariantAgentsServiceResponse",
    "ApplicationVariantAgentsServiceResponseConfiguration",
    "ApplicationVariantAgentsServiceResponseConfigurationGraph",
    "ApplicationVariantAgentsServiceResponseConfigurationGraphEdge",
    "ApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig",
    "ApplicationVariantAgentsServiceResponseConfigurationInput",
    "ApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint",
    "ApplicationVariantAgentsServiceResponseConfigurationInputsByNode",
    "ApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint",
    "OfflineApplicationVariantResponse",
    "OfflineApplicationVariantResponseConfiguration",
    "OfflineApplicationVariantResponseConfigurationGuardrailConfig",
]


class ApplicationVariantV0Response(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: ApplicationConfiguration

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    draft: bool
    """Boolean to indicate whether the variant is in draft mode"""

    name: str

    updated_at: datetime
    """The date and time when the entity was last updated in ISO format."""

    version: Literal["V0"]

    created_by_user_id: Optional[str] = None
    """The user who originally created the entity."""

    description: Optional[str] = None
    """Optional description of the application variant"""

    published_at: Optional[datetime] = None
    """The date and time that the variant was published."""


class ApplicationVariantAgentsServiceResponseConfigurationGraphEdge(BaseModel):
    from_node: str

    to_node: str


class ApplicationVariantAgentsServiceResponseConfigurationGraph(BaseModel):
    edges: List[ApplicationVariantAgentsServiceResponseConfigurationGraphEdge]

    nodes: List["ApplicationAgentGraphNode"]


class ApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig(BaseModel):
    guardrails_to_execute: List[str]
    """List of guardrail ids that need to be executed for the application interactions"""


class ApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint(BaseModel):
    potential_values: List[str]

    selection_constraint_type: Literal["single", "multi"]

    value_type: Literal[
        "ShortText",
        "SentenceText",
        "ParagraphText",
        "ArtifactId",
        "ArtifactIds",
        "KnowledgeBaseId",
        "KnowledgeBaseIds",
        "InputImageDir",
        "Message",
        "Messages",
        "integer",
        "number",
        "string",
        "boolean",
        "array",
        "object",
        "unknown",
    ]


class ApplicationVariantAgentsServiceResponseConfigurationInput(BaseModel):
    name: str

    type: Literal[
        "ShortText",
        "SentenceText",
        "ParagraphText",
        "ArtifactId",
        "ArtifactIds",
        "KnowledgeBaseId",
        "KnowledgeBaseIds",
        "InputImageDir",
        "Message",
        "Messages",
        "integer",
        "number",
        "string",
        "boolean",
        "array",
        "object",
        "unknown",
    ]

    default: Optional[str] = None

    description: Optional[str] = None

    examples: Optional[List[str]] = None

    required: Optional[bool] = None

    title: Optional[str] = None

    value_constraint: Optional[ApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint] = None


class ApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint(BaseModel):
    potential_values: List[str]

    selection_constraint_type: Literal["single", "multi"]

    value_type: Literal[
        "ShortText",
        "SentenceText",
        "ParagraphText",
        "ArtifactId",
        "ArtifactIds",
        "KnowledgeBaseId",
        "KnowledgeBaseIds",
        "InputImageDir",
        "Message",
        "Messages",
        "integer",
        "number",
        "string",
        "boolean",
        "array",
        "object",
        "unknown",
    ]


class ApplicationVariantAgentsServiceResponseConfigurationInputsByNode(BaseModel):
    name: str

    type: Literal[
        "ShortText",
        "SentenceText",
        "ParagraphText",
        "ArtifactId",
        "ArtifactIds",
        "KnowledgeBaseId",
        "KnowledgeBaseIds",
        "InputImageDir",
        "Message",
        "Messages",
        "integer",
        "number",
        "string",
        "boolean",
        "array",
        "object",
        "unknown",
    ]

    default: Optional[str] = None

    description: Optional[str] = None

    examples: Optional[List[str]] = None

    required: Optional[bool] = None

    title: Optional[str] = None

    value_constraint: Optional[ApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint] = None


class ApplicationVariantAgentsServiceResponseConfiguration(BaseModel):
    params: object

    type: Literal["WORKFLOW", "PLAN", "STATE_MACHINE"]

    agent_service_errors: Optional[List[str]] = None
    """Errors that occurred when calling agent service"""

    graph: Optional[ApplicationVariantAgentsServiceResponseConfigurationGraph] = None
    """The graph of the agents service configuration"""

    guardrail_config: Optional[ApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig] = None
    """Guardrail configuration for the application"""

    inputs: Optional[List[ApplicationVariantAgentsServiceResponseConfigurationInput]] = None
    """The starting inputs that this agent configuration expects"""

    inputs_by_node: Optional[Dict[str, List[ApplicationVariantAgentsServiceResponseConfigurationInputsByNode]]] = None
    """The inputs that each node expects"""

    metadata: Optional[object] = None
    """User defined metadata about the application"""

    raw_configuration: Optional[str] = None
    """Raw configuration entered by the user.

    May be invalid if variant is in draft mode.
    """


class ApplicationVariantAgentsServiceResponse(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: ApplicationVariantAgentsServiceResponseConfiguration

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    draft: bool
    """Boolean to indicate whether the variant is in draft mode"""

    name: str

    updated_at: datetime
    """The date and time when the entity was last updated in ISO format."""

    version: Literal["AGENTS_SERVICE"]

    created_by_user_id: Optional[str] = None
    """The user who originally created the entity."""

    description: Optional[str] = None
    """Optional description of the application variant"""

    published_at: Optional[datetime] = None
    """The date and time that the variant was published."""


class OfflineApplicationVariantResponseConfigurationGuardrailConfig(BaseModel):
    guardrails_to_execute: List[str]
    """List of guardrail ids that need to be executed for the application interactions"""


class OfflineApplicationVariantResponseConfiguration(BaseModel):
    guardrail_config: Optional[OfflineApplicationVariantResponseConfigurationGuardrailConfig] = None
    """Guardrail configuration for the application"""

    metadata: Optional[object] = None
    """User defined metadata about the application"""


class OfflineApplicationVariantResponse(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: OfflineApplicationVariantResponseConfiguration

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    draft: bool
    """Boolean to indicate whether the variant is in draft mode"""

    name: str

    updated_at: datetime
    """The date and time when the entity was last updated in ISO format."""

    version: Literal["OFFLINE"]

    created_by_user_id: Optional[str] = None
    """The user who originally created the entity."""

    description: Optional[str] = None
    """Optional description of the application variant"""

    published_at: Optional[datetime] = None
    """The date and time that the variant was published."""


ApplicationVariantCreateResponse: TypeAlias = Annotated[
    Union[ApplicationVariantV0Response, ApplicationVariantAgentsServiceResponse, OfflineApplicationVariantResponse],
    PropertyInfo(discriminator="version"),
]

from .application_agent_graph_node import ApplicationAgentGraphNode

if PYDANTIC_V2:
    ApplicationVariantV0Response.model_rebuild()
    ApplicationVariantAgentsServiceResponse.model_rebuild()
    ApplicationVariantAgentsServiceResponseConfiguration.model_rebuild()
    ApplicationVariantAgentsServiceResponseConfigurationGraph.model_rebuild()
    ApplicationVariantAgentsServiceResponseConfigurationGraphEdge.model_rebuild()
    ApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig.model_rebuild()
    ApplicationVariantAgentsServiceResponseConfigurationInput.model_rebuild()
    ApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint.model_rebuild()
    ApplicationVariantAgentsServiceResponseConfigurationInputsByNode.model_rebuild()
    ApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint.model_rebuild()
    OfflineApplicationVariantResponse.model_rebuild()
    OfflineApplicationVariantResponseConfiguration.model_rebuild()
    OfflineApplicationVariantResponseConfigurationGuardrailConfig.model_rebuild()
else:
    ApplicationVariantV0Response.update_forward_refs()  # type: ignore
    ApplicationVariantAgentsServiceResponse.update_forward_refs()  # type: ignore
    ApplicationVariantAgentsServiceResponseConfiguration.update_forward_refs()  # type: ignore
    ApplicationVariantAgentsServiceResponseConfigurationGraph.update_forward_refs()  # type: ignore
    ApplicationVariantAgentsServiceResponseConfigurationGraphEdge.update_forward_refs()  # type: ignore
    ApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig.update_forward_refs()  # type: ignore
    ApplicationVariantAgentsServiceResponseConfigurationInput.update_forward_refs()  # type: ignore
    ApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint.update_forward_refs()  # type: ignore
    ApplicationVariantAgentsServiceResponseConfigurationInputsByNode.update_forward_refs()  # type: ignore
    ApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint.update_forward_refs()  # type: ignore
    OfflineApplicationVariantResponse.update_forward_refs()  # type: ignore
    OfflineApplicationVariantResponseConfiguration.update_forward_refs()  # type: ignore
    OfflineApplicationVariantResponseConfigurationGuardrailConfig.update_forward_refs()  # type: ignore
