import logging

from sqlalchemy.orm import Session

from app.modules.dashboard.repository import (
    DashboardRepository,
)
from app.modules.dashboard.schemas import (
    DashboardActivity,
    DashboardSummary,
)

logger = logging.getLogger(__name__)


class DashboardService:
    """
    Business logic for dashboard operations.
    """

    def __init__(self, db: Session):
        self.repository = DashboardRepository(db)

    def get_summary(self) -> DashboardSummary:
        logger.info("Fetching dashboard summary")

        total_customers = self.repository.count_customers()

        active_customers = self.repository.count_active_customers()

        new_customers = self.repository.count_new_customers_this_month()

        organizations = self.repository.count_organizations()

        recent_activity = self.repository.get_recent_activity()

        return DashboardSummary(
            total_customers=total_customers,
            active_customers=active_customers,
            new_customers=new_customers,
            organizations=organizations,
            recent_activity=[
                DashboardActivity.model_validate(
                    activity,
                )
                for activity in recent_activity
            ],
        )
