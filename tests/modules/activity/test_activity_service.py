from app.modules.activity.enums import (
    ActivityAction,
    EntityType,
)
from app.modules.activity.schemas import ActivityCreate
from app.modules.activity.service import ActivityService


def test_log_activity(db_session):
    service = ActivityService(db_session)

    activity = ActivityCreate(
        entity_type=EntityType.CUSTOMER,
        entity_id="customer-123",
        action=ActivityAction.CREATED,
        performed_by="user-123",
        details={
            "email": "john@example.com",
        },
    )

    result = service.log(activity)

    assert result.id is not None
    assert result.entity_type == EntityType.CUSTOMER
    assert result.entity_id == "customer-123"
    assert result.action == ActivityAction.CREATED
    assert result.performed_by == "user-123"
    assert result.details["email"] == "john@example.com"
