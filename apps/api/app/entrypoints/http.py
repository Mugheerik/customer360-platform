from fastapi import APIRouter

from app.modules.customers.router import router as customer_router
from app.modules.health.router import router as health_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(customer_router)
