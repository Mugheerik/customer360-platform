from fastapi import FastAPI
from app.entrypoints.http import api_router

app = FastAPI(
    title="Customer360 API",
    description="Enterprise Customer360 Platform",
    version="0.1.0",
)

app.include_router(api_router)