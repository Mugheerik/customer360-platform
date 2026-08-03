from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.modules.activity.enums import (
    ActivityAction,
    EntityType,
)


class ActivityCreate(BaseModel):
    entity_type: EntityType
    entity_id: str
    action: ActivityAction
    performed_by: str | None = None
    details: dict | None = None


class ActivityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    entity_type: EntityType
    entity_id: str
    action: ActivityAction
    performed_by: str | None
    details: dict | None
    created_at: datetime
