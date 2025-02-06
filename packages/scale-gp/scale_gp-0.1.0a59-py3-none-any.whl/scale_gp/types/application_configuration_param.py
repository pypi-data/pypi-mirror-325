# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .application_edge_param import ApplicationEdgeParam
from .application_node_param import ApplicationNodeParam

__all__ = ["ApplicationConfigurationParam", "GuardrailConfig"]


class GuardrailConfig(TypedDict, total=False):
    guardrails_to_execute: Required[List[str]]
    """List of guardrail ids that need to be executed for the application interactions"""


class ApplicationConfigurationParam(TypedDict, total=False):
    edges: Required[Iterable[ApplicationEdgeParam]]

    nodes: Required[Iterable[ApplicationNodeParam]]

    guardrail_config: GuardrailConfig
    """Guardrail configuration for the application"""

    metadata: object
    """User defined metadata about the application"""
