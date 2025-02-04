# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VoiceCreateParams"]


class VoiceCreateParams(TypedDict, total=False):
    flow_id: Required[Annotated[str, PropertyInfo(alias="flowId")]]

    name: Required[str]

    config: object

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]

    voice_id: Annotated[str, PropertyInfo(alias="voiceId")]

    voice_provider: Annotated[str, PropertyInfo(alias="voiceProvider")]
