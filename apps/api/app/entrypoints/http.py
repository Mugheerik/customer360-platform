from app.modules.activity.router import router as activity_router
from app.modules.auth.router import router as auth_router
from app.modules.customers.router import router as customer_router
from app.modules.health.router import router as health_router
from app.modules.notes.router import router as notes_router
from app.modules.tasks.router import router as task_router
from app.modules.users.router import router as users_router
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(customer_router)
api_router.include_router(activity_router)
api_router.include_router(notes_router)
api_router.include_router(task_router)
