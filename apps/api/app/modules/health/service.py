from app.core.config import settings
from app.modules.health.schemas import HealthResponse


class HealthService:
    """
    Business logic for application health.
    """

    def get_health(self) -> HealthResponse:
        return HealthResponse(
            status="healthy",
            service=settings.app_name,
            version=settings.app_version,
        )