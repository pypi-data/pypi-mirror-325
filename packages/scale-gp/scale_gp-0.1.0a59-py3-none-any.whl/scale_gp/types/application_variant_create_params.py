# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .application_configuration_param import ApplicationConfigurationParam

__all__ = [
    "ApplicationVariantCreateParams",
    "ApplicationVariantV0Request",
    "ApplicationVariantAgentsServiceRequest",
    "ApplicationVariantAgentsServiceRequestConfiguration",
    "ApplicationVariantAgentsServiceRequestConfigurationGraph",
    "ApplicationVariantAgentsServiceRequestConfigurationGraphEdge",
    "ApplicationVariantAgentsServiceRequestConfigurationGuardrailConfig",
    "ApplicationVariantAgentsServiceRequestConfigurationInput",
    "ApplicationVariantAgentsServiceRequestConfigurationInputValueConstraint",
    "ApplicationVariantAgentsServiceRequestConfigurationInputsByNode",
    "ApplicationVariantAgentsServiceRequestConfigurationInputsByNodeValueConstraint",
    "OfflineApplicationVariantRequest",
    "OfflineApplicationVariantRequestConfiguration",
    "OfflineApplicationVariantRequestConfigurationGuardrailConfig",
]


class ApplicationVariantV0Request(TypedDict, total=False):
    account_id: Required[str]
    """The ID of the account that owns the given entity."""

    application_spec_id: Required[str]

    configuration: Required[ApplicationConfigurationParam]

    name: Required[str]

    version: Required[Literal["V0"]]

    description: str
    """Optional description of the application variant"""

    draft: bool
    """Boolean to indicate whether the variant is in draft mode"""

    published_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date and time that the variant was published."""


class ApplicationVariantAgentsServiceRequest(TypedDict, total=False):
    account_id: Required[str]
    """The ID of the account that owns the given entity."""

    application_spec_id: Required[str]

    configuration: Required[ApplicationVariantAgentsServiceRequestConfiguration]

    name: Required[str]

    version: Required[Literal["AGENTS_SERVICE"]]

    description: str
    """Optional description of the application variant"""

    draft: bool
    """Boolean to indicate whether the variant is in draft mode"""

    published_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date and time that the variant was published."""


class ApplicationVariantAgentsServiceRequestConfigurationGraphEdge(TypedDict, total=False):
    from_node: Required[str]

    to_node: Required[str]


class ApplicationVariantAgentsServiceRequestConfigurationGraph(TypedDict, total=False):
    edges: Required[Iterable[ApplicationVariantAgentsServiceRequestConfigurationGraphEdge]]

    nodes: Required[Iterable["ApplicationAgentGraphNodeParam"]]


class ApplicationVariantAgentsServiceRequestConfigurationGuardrailConfig(TypedDict, total=False):
    guardrails_to_execute: Required[List[str]]
    """List of guardrail ids that need to be executed for the application interactions"""


class ApplicationVariantAgentsServiceRequestConfigurationInputValueConstraint(TypedDict, total=False):
    potential_values: Required[List[str]]

    selection_constraint_type: Required[Literal["single", "multi"]]

    value_type: Required[
        Literal[
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
    ]


class ApplicationVariantAgentsServiceRequestConfigurationInput(TypedDict, total=False):
    name: Required[str]

    type: Required[
        Literal[
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
    ]

    default: str

    description: str

    examples: List[str]

    required: bool

    title: str

    value_constraint: ApplicationVariantAgentsServiceRequestConfigurationInputValueConstraint


class ApplicationVariantAgentsServiceRequestConfigurationInputsByNodeValueConstraint(TypedDict, total=False):
    potential_values: Required[List[str]]

    selection_constraint_type: Required[Literal["single", "multi"]]

    value_type: Required[
        Literal[
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
    ]


class ApplicationVariantAgentsServiceRequestConfigurationInputsByNode(TypedDict, total=False):
    name: Required[str]

    type: Required[
        Literal[
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
    ]

    default: str

    description: str

    examples: List[str]

    required: bool

    title: str

    value_constraint: ApplicationVariantAgentsServiceRequestConfigurationInputsByNodeValueConstraint


class ApplicationVariantAgentsServiceRequestConfiguration(TypedDict, total=False):
    params: Required[object]

    type: Required[Literal["WORKFLOW", "PLAN", "STATE_MACHINE"]]

    agent_service_errors: List[str]
    """Errors that occurred when calling agent service"""

    graph: ApplicationVariantAgentsServiceRequestConfigurationGraph
    """The graph of the agents service configuration"""

    guardrail_config: ApplicationVariantAgentsServiceRequestConfigurationGuardrailConfig
    """Guardrail configuration for the application"""

    inputs: Iterable[ApplicationVariantAgentsServiceRequestConfigurationInput]
    """The starting inputs that this agent configuration expects"""

    inputs_by_node: Dict[str, Iterable[ApplicationVariantAgentsServiceRequestConfigurationInputsByNode]]
    """The inputs that each node expects"""

    metadata: object
    """User defined metadata about the application"""

    raw_configuration: str
    """Raw configuration entered by the user.

    May be invalid if variant is in draft mode.
    """


class OfflineApplicationVariantRequest(TypedDict, total=False):
    account_id: Required[str]
    """The ID of the account that owns the given entity."""

    application_spec_id: Required[str]

    configuration: Required[OfflineApplicationVariantRequestConfiguration]

    name: Required[str]

    version: Required[Literal["OFFLINE"]]

    description: str
    """Optional description of the application variant"""

    draft: bool
    """Boolean to indicate whether the variant is in draft mode"""

    published_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date and time that the variant was published."""


class OfflineApplicationVariantRequestConfigurationGuardrailConfig(TypedDict, total=False):
    guardrails_to_execute: Required[List[str]]
    """List of guardrail ids that need to be executed for the application interactions"""


class OfflineApplicationVariantRequestConfiguration(TypedDict, total=False):
    guardrail_config: OfflineApplicationVariantRequestConfigurationGuardrailConfig
    """Guardrail configuration for the application"""

    metadata: object
    """User defined metadata about the application"""


ApplicationVariantCreateParams: TypeAlias = Union[
    ApplicationVariantV0Request, ApplicationVariantAgentsServiceRequest, OfflineApplicationVariantRequest
]

from .application_agent_graph_node_param import ApplicationAgentGraphNodeParam
