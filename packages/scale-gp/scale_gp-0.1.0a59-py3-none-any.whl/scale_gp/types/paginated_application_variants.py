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
    "PaginatedApplicationVariants",
    "Item",
    "ItemApplicationVariantV0Response",
    "ItemApplicationVariantAgentsServiceResponse",
    "ItemApplicationVariantAgentsServiceResponseConfiguration",
    "ItemApplicationVariantAgentsServiceResponseConfigurationGraph",
    "ItemApplicationVariantAgentsServiceResponseConfigurationGraphEdge",
    "ItemApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig",
    "ItemApplicationVariantAgentsServiceResponseConfigurationInput",
    "ItemApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint",
    "ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNode",
    "ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint",
    "ItemOfflineApplicationVariantResponse",
    "ItemOfflineApplicationVariantResponseConfiguration",
    "ItemOfflineApplicationVariantResponseConfigurationGuardrailConfig",
]


class ItemApplicationVariantV0Response(BaseModel):
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


class ItemApplicationVariantAgentsServiceResponseConfigurationGraphEdge(BaseModel):
    from_node: str

    to_node: str


class ItemApplicationVariantAgentsServiceResponseConfigurationGraph(BaseModel):
    edges: List[ItemApplicationVariantAgentsServiceResponseConfigurationGraphEdge]

    nodes: List["ApplicationAgentGraphNode"]


class ItemApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig(BaseModel):
    guardrails_to_execute: List[str]
    """List of guardrail ids that need to be executed for the application interactions"""


class ItemApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint(BaseModel):
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


class ItemApplicationVariantAgentsServiceResponseConfigurationInput(BaseModel):
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

    value_constraint: Optional[ItemApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint] = None


class ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint(BaseModel):
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


class ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNode(BaseModel):
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

    value_constraint: Optional[ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint] = (
        None
    )


class ItemApplicationVariantAgentsServiceResponseConfiguration(BaseModel):
    params: object

    type: Literal["WORKFLOW", "PLAN", "STATE_MACHINE"]

    agent_service_errors: Optional[List[str]] = None
    """Errors that occurred when calling agent service"""

    graph: Optional[ItemApplicationVariantAgentsServiceResponseConfigurationGraph] = None
    """The graph of the agents service configuration"""

    guardrail_config: Optional[ItemApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig] = None
    """Guardrail configuration for the application"""

    inputs: Optional[List[ItemApplicationVariantAgentsServiceResponseConfigurationInput]] = None
    """The starting inputs that this agent configuration expects"""

    inputs_by_node: Optional[Dict[str, List[ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNode]]] = (
        None
    )
    """The inputs that each node expects"""

    metadata: Optional[object] = None
    """User defined metadata about the application"""

    raw_configuration: Optional[str] = None
    """Raw configuration entered by the user.

    May be invalid if variant is in draft mode.
    """


class ItemApplicationVariantAgentsServiceResponse(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: ItemApplicationVariantAgentsServiceResponseConfiguration

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


class ItemOfflineApplicationVariantResponseConfigurationGuardrailConfig(BaseModel):
    guardrails_to_execute: List[str]
    """List of guardrail ids that need to be executed for the application interactions"""


class ItemOfflineApplicationVariantResponseConfiguration(BaseModel):
    guardrail_config: Optional[ItemOfflineApplicationVariantResponseConfigurationGuardrailConfig] = None
    """Guardrail configuration for the application"""

    metadata: Optional[object] = None
    """User defined metadata about the application"""


class ItemOfflineApplicationVariantResponse(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    application_spec_id: str

    configuration: ItemOfflineApplicationVariantResponseConfiguration

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


Item: TypeAlias = Annotated[
    Union[
        ItemApplicationVariantV0Response,
        ItemApplicationVariantAgentsServiceResponse,
        ItemOfflineApplicationVariantResponse,
    ],
    PropertyInfo(discriminator="version"),
]


class PaginatedApplicationVariants(BaseModel):
    current_page: int
    """The current page number."""

    items: List[Item]
    """The data returned for the current page."""

    items_per_page: int
    """The number of items per page."""

    total_item_count: int
    """The total number of items of the query"""


from .application_agent_graph_node import ApplicationAgentGraphNode

if PYDANTIC_V2:
    PaginatedApplicationVariants.model_rebuild()
    ItemApplicationVariantV0Response.model_rebuild()
    ItemApplicationVariantAgentsServiceResponse.model_rebuild()
    ItemApplicationVariantAgentsServiceResponseConfiguration.model_rebuild()
    ItemApplicationVariantAgentsServiceResponseConfigurationGraph.model_rebuild()
    ItemApplicationVariantAgentsServiceResponseConfigurationGraphEdge.model_rebuild()
    ItemApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig.model_rebuild()
    ItemApplicationVariantAgentsServiceResponseConfigurationInput.model_rebuild()
    ItemApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint.model_rebuild()
    ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNode.model_rebuild()
    ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint.model_rebuild()
    ItemOfflineApplicationVariantResponse.model_rebuild()
    ItemOfflineApplicationVariantResponseConfiguration.model_rebuild()
    ItemOfflineApplicationVariantResponseConfigurationGuardrailConfig.model_rebuild()
else:
    PaginatedApplicationVariants.update_forward_refs()  # type: ignore
    ItemApplicationVariantV0Response.update_forward_refs()  # type: ignore
    ItemApplicationVariantAgentsServiceResponse.update_forward_refs()  # type: ignore
    ItemApplicationVariantAgentsServiceResponseConfiguration.update_forward_refs()  # type: ignore
    ItemApplicationVariantAgentsServiceResponseConfigurationGraph.update_forward_refs()  # type: ignore
    ItemApplicationVariantAgentsServiceResponseConfigurationGraphEdge.update_forward_refs()  # type: ignore
    ItemApplicationVariantAgentsServiceResponseConfigurationGuardrailConfig.update_forward_refs()  # type: ignore
    ItemApplicationVariantAgentsServiceResponseConfigurationInput.update_forward_refs()  # type: ignore
    ItemApplicationVariantAgentsServiceResponseConfigurationInputValueConstraint.update_forward_refs()  # type: ignore
    ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNode.update_forward_refs()  # type: ignore
    ItemApplicationVariantAgentsServiceResponseConfigurationInputsByNodeValueConstraint.update_forward_refs()  # type: ignore
    ItemOfflineApplicationVariantResponse.update_forward_refs()  # type: ignore
    ItemOfflineApplicationVariantResponseConfiguration.update_forward_refs()  # type: ignore
    ItemOfflineApplicationVariantResponseConfigurationGuardrailConfig.update_forward_refs()  # type: ignore
