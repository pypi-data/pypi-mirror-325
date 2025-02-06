# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .application_edge import ApplicationEdge
from .application_node import ApplicationNode

__all__ = ["ApplicationConfiguration", "GuardrailConfig"]


class GuardrailConfig(BaseModel):
    guardrails_to_execute: List[str]
    """List of guardrail ids that need to be executed for the application interactions"""


class ApplicationConfiguration(BaseModel):
    edges: List[ApplicationEdge]

    nodes: List[ApplicationNode]

    guardrail_config: Optional[GuardrailConfig] = None
    """Guardrail configuration for the application"""

    metadata: Optional[object] = None
    """User defined metadata about the application"""
