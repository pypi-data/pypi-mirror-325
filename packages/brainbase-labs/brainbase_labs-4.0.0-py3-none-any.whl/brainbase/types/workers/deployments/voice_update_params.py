# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VoiceUpdateParams"]


class VoiceUpdateParams(TypedDict, total=False):
    worker_id: Required[Annotated[str, PropertyInfo(alias="workerId")]]

    name: Required[str]
    """Name of the voice deployment"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number for the voice deployment"""

    voice_id: Annotated[str, PropertyInfo(alias="voiceId")]
    """Voice ID for the deployment"""

    voice_provider: Annotated[str, PropertyInfo(alias="voiceProvider")]
    """Voice provider service"""
