# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FlowCreateParams"]


class FlowCreateParams(TypedDict, total=False):
    code: Required[str]
    """Flow code"""

    name: Required[str]
    """Name of the flow"""

    label: str
    """Optional label for the flow"""
