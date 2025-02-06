# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MultiturnAnnotationConfigParam", "LlmPrompt", "LlmPromptVariable"]


class LlmPromptVariable(TypedDict, total=False):
    data_loc: Required[List[str]]

    name: Required[str]

    optional: bool


class LlmPrompt(TypedDict, total=False):
    template: Required[str]

    variables: Required[Iterable[LlmPromptVariable]]


class MultiturnAnnotationConfigParam(TypedDict, total=False):
    messages_loc: Required[List[str]]

    llm_prompt: LlmPrompt
