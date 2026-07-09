from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import CustomerNotFoundError


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(CustomerNotFoundError)
    async def customer_not_found_handler(
        request: Request,
        exc: CustomerNotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "error": {
                    "code": "CUSTOMER_NOT_FOUND",
                    "message": exc.message,
                }
            },
        )