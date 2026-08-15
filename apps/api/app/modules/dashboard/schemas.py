from datetime import datetime
from typing import Any

from pydantic import BaseModel


class DashboardActivity(BaseModel):
    id: str
    entity_type: str
    entity_id: str
    action: str
    actor_id: str | None
    details: dict[str, Any] | None
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }


class DashboardSummary(BaseModel):
    total_customers: int
    active_customers: int
    new_customers: int
    organizations: int
    recent_activity: list[DashboardActivity]
