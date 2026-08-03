from app.core.security.dependencies import get_current_user
from app.database.dependencies import get_db
from app.modules.auth.schemas import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
)
from app.modules.auth.service import AuthService
from app.modules.users.models import User
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
) -> RegisterResponse:
    """
    Register a new user.
    """
    service = AuthService(db)

    user = service.register(request)

    return RegisterResponse.model_validate(user)


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
) -> LoginResponse:
    """
    Authenticate a user.
    """
    service = AuthService(db)

    access_token = service.login(request)

    return LoginResponse(
        access_token=access_token,
    )


@router.get(
    "/me",
    response_model=RegisterResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
) -> RegisterResponse:
    """
    Return the authenticated user.
    """
    return RegisterResponse.model_validate(current_user)
