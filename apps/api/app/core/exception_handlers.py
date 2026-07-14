from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    ConflictError,
    CustomerNotFoundError,
    ForbiddenError,
    UnauthorizedError,
)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers.
    """

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

    @app.exception_handler(ConflictError)
    async def conflict_handler(
        request: Request,
        exc: ConflictError,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "error": {
                    "code": "CONFLICT",
                    "message": str(exc),
                }
            },
        )

    @app.exception_handler(UnauthorizedError)
    async def unauthorized_handler(
        request: Request,
        exc: UnauthorizedError,
    ):
        return JSONResponse(
            status_code=401,
            content={
                "error": {
                    "code": "UNAUTHORIZED",
                    "message": str(exc),
                }
            },
        )

    @app.exception_handler(ForbiddenError)
    async def forbidden_handler(
        request: Request,
        exc: ForbiddenError,
    ):
        return JSONResponse(
            status_code=403,
            content={
                "error": {
                    "code": "FORBIDDEN",
                    "message": str(exc),
                }
            },
        )
