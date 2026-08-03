from app.modules.activity.enums import EntityType
from app.modules.activity.models import ActivityLog
from app.modules.activity.schemas import ActivityCreate
from sqlalchemy import select
from sqlalchemy.orm import Session


class ActivityRepository:
    """
    Handles persistence and queries for activity logs.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        activity: ActivityCreate,
    ) -> ActivityLog:
        db_activity = ActivityLog(
            entity_type=activity.entity_type,
            entity_id=activity.entity_id,
            action=activity.action,
            performed_by=activity.performed_by,
            details=activity.details,
        )

        self.db.add(db_activity)
        self.db.flush()
        self.db.refresh(db_activity)

        return db_activity

    def get_customer_timeline(
        self,
        customer_id: str,
    ) -> list[ActivityLog]:
        """
        Retrieve the activity timeline for a customer.

        Results are ordered newest first.
        """

        statement = (
            select(ActivityLog)
            .where(
                ActivityLog.entity_type == EntityType.CUSTOMER,
                ActivityLog.entity_id == customer_id,
            )
            .order_by(ActivityLog.created_at.desc())
        )

        return list(self.db.scalars(statement).all())
