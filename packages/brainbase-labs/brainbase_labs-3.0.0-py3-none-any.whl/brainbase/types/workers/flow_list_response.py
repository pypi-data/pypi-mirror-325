# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowListResponse", "FlowListResponseItem"]


class FlowListResponseItem(BaseModel):
    id: str

    code: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int

    worker_id: str = FieldInfo(alias="workerId")

    deployments_ids: Optional[List[str]] = FieldInfo(alias="deploymentsIds", default=None)

    label: Optional[str] = None


FlowListResponse: TypeAlias = List[FlowListResponseItem]
