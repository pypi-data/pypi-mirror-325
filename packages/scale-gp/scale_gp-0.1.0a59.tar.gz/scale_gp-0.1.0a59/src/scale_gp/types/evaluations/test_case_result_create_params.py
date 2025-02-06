# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TestCaseResultCreateParams"]


class TestCaseResultCreateParams(TypedDict, total=False):
    application_spec_id: Required[str]

    evaluation_dataset_version_num: Required[str]

    test_case_evaluation_data: Required[object]

    test_case_id: Required[str]

    account_id: str

    annotated_by_user_id: str

    audit_comment: str

    audit_required: bool

    audit_status: Literal["UNAUDITED", "FIXED", "APPROVED"]

    label_status: Literal["PENDING", "COMPLETED", "FAILED"]

    result: Dict[str, Union[str, bool, float, List[Union[str, bool, float]]]]

    time_spent_labeling_s: int
