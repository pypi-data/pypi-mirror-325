# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["VoiceCreateResponse"]


class VoiceCreateResponse(BaseModel):
    id: str

    delegate_aux_deployments_id: Optional[str] = FieldInfo(alias="delegate_aux_deploymentsId", default=None)

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_provider: Optional[str] = FieldInfo(alias="voiceProvider", default=None)
