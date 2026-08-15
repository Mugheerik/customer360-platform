from datetime import UTC, datetime

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.modules.activity.models import ActivityLog
from app.modules.customers.enums import CustomerStatus
from app.modules.customers.models import Customer


class DashboardRepository:
    """
    Read-only database queries used by the dashboard.
    """

    def __init__(self, db: Session):
        self.db = db

    def count_customers(self) -> int:
        statement = select(
            func.count(),
        ).select_from(Customer)

        return self.db.scalar(statement) or 0

    def count_active_customers(self) -> int:
        statement = (
            select(func.count())
            .select_from(Customer)
            .where(
                Customer.status == CustomerStatus.ACTIVE,
            )
        )

        return self.db.scalar(statement) or 0

    def count_new_customers_this_month(self) -> int:
        now = datetime.now(UTC)

        month_start = now.replace(
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

        statement = (
            select(func.count())
            .select_from(Customer)
            .where(
                Customer.created_at >= month_start,
            )
        )

        return self.db.scalar(statement) or 0

    def count_organizations(self) -> int:
        """
        Organizations are not implemented as a domain yet.

        Keep the dashboard contract stable while the
        organization domain is introduced later.
        """
        return 0

    def get_recent_activity(
        self,
        limit: int = 10,
    ) -> list[ActivityLog]:
        statement = (
            select(ActivityLog)
            .order_by(
                ActivityLog.created_at.desc(),
            )
            .limit(limit)
        )

        return list(
            self.db.scalars(statement).all(),
        )
