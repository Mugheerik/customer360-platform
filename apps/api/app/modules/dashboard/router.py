from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security.dependencies import (
    get_current_user,
)
from app.database.dependencies import get_db
from app.modules.dashboard.schemas import DashboardSummary
from app.modules.dashboard.service import DashboardService
from app.modules.users.models import User

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


def get_dashboard_service(
    db: Session = Depends(get_db),
) -> DashboardService:
    return DashboardService(db)


@router.get(
    "/summary",
    response_model=DashboardSummary,
)
def get_dashboard_summary(
    current_user: User = Depends(
        get_current_user,
    ),
    service: DashboardService = Depends(
        get_dashboard_service,
    ),
) -> DashboardSummary:
    return service.get_summary()
