import logging

from app.core.uow import UnitOfWork
from app.modules.activity.models import ActivityLog
from app.modules.activity.schemas import ActivityCreate
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


class ActivityService:
    """
    Business logic for activity operations.
    """

    def __init__(
        self,
        db: Session | UnitOfWork,
    ):
        if isinstance(db, UnitOfWork):
            self.uow = db
        else:
            self.uow = UnitOfWork(db)

        self.activities = self.uow.activities

    def log(
        self,
        activity: ActivityCreate,
    ) -> ActivityLog:
        logger.info(
            "Creating activity '%s' for %s '%s'",
            activity.action.value,
            activity.entity_type.value,
            activity.entity_id,
        )

        activity_log = self.activities.create(activity)

        logger.info(
            "Activity prepared successfully.",
        )

        return activity_log

    def create(
        self,
        activity: ActivityCreate,
    ) -> ActivityLog:
        return self.log(activity)

    def get_customer_timeline(
        self,
        customer_id: str,
    ) -> list[ActivityLog]:
        """
        Retrieve the complete activity timeline for a customer.
        """

        logger.info(
            "Fetching timeline for customer '%s'",
            customer_id,
        )

        timeline = self.activities.get_customer_timeline(
            customer_id,
        )

        logger.info(
            "Retrieved %d timeline events",
            len(timeline),
        )

        return timeline
