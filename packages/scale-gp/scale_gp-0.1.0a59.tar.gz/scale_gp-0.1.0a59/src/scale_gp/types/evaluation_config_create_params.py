# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "EvaluationConfigCreateParams",
    "AutoEvalEvaluationConfigRequest",
    "AutoEvalEvaluationConfigRequestAutoEvaluationParameters",
    "ManualEvaluationConfigRequest",
    "ManualEvaluationConfigRequestAutoEvaluationParameters",
]


class AutoEvalEvaluationConfigRequest(TypedDict, total=False):
    account_id: Required[str]
    """The ID of the account that owns the given entity."""

    question_set_id: Required[str]

    auto_evaluation_model: Literal["llama-3-1-70b-instruct", "gpt-4-turbo-2024-04-09"]
    """The name of the model to be used for auto-evaluation"""

    auto_evaluation_parameters: AutoEvalEvaluationConfigRequestAutoEvaluationParameters
    """Execution parameters for auto-evaluation"""

    evaluation_type: Literal["llm_auto", "llm_benchmark"]
    """Evaluation type"""

    studio_project_id: str


class AutoEvalEvaluationConfigRequestAutoEvaluationParameters(TypedDict, total=False):
    batch_size: int

    temperature: float


class ManualEvaluationConfigRequest(TypedDict, total=False):
    account_id: Required[str]
    """The ID of the account that owns the given entity."""

    question_set_id: Required[str]

    auto_evaluation_model: None
    """The name of the model to be used for auto-evaluation.

    Not applicable for manual evaluations.
    """

    auto_evaluation_parameters: ManualEvaluationConfigRequestAutoEvaluationParameters
    """Execution parameters for auto-evaluation"""

    evaluation_type: Literal["studio", "human"]
    """Evaluation type"""

    studio_project_id: str


class ManualEvaluationConfigRequestAutoEvaluationParameters(TypedDict, total=False):
    batch_size: int

    temperature: float


EvaluationConfigCreateParams: TypeAlias = Union[AutoEvalEvaluationConfigRequest, ManualEvaluationConfigRequest]
