# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkerCreateResponse"]


class WorkerCreateResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    team_id: str = FieldInfo(alias="teamId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    deployments_ids: Optional[List[str]] = FieldInfo(alias="deploymentsIds", default=None)

    description: Optional[str] = None

    flows_ids: Optional[List[str]] = FieldInfo(alias="flowsIds", default=None)

    integrations_ids: Optional[List[str]] = FieldInfo(alias="integrationsIds", default=None)

    last_refreshed_at: Optional[datetime] = FieldInfo(alias="lastRefreshedAt", default=None)

    resources_ids: Optional[List[str]] = FieldInfo(alias="resourcesIds", default=None)

    status: Optional[str] = None
