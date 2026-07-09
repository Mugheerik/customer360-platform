from fastapi import APIRouter

from app.modules.health.schemas import HealthResponse
from app.modules.health.service import HealthService

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    response_model=HealthResponse,
)
def health_check() -> HealthResponse:
    service = HealthService()
    return service.get_health()