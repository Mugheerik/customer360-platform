from fastapi import FastAPI

from app.core.exception_handlers import register_exception_handlers
from app.entrypoints.http import api_router

app = FastAPI(
    title="Customer360 API",
    version="0.3.0",
)

register_exception_handlers(app)

app.include_router(api_router)