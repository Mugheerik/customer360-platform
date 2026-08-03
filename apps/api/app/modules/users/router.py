from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security.dependencies import (
    get_current_user,
    require_superuser,
)
from app.core.uow import UnitOfWork
from app.database.dependencies import get_db
from app.modules.users.models import User
from app.modules.users.schemas import UserResponse
from app.modules.users.service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


def get_user_service(
    db: Session = Depends(get_db),
) -> UserService:
    return UserService(UnitOfWork(db))


@router.get(
    "",
    response_model=list[UserResponse],
)
def list_users(
    service: UserService = Depends(get_user_service),
    _: User = Depends(require_superuser),
) -> list[UserResponse]:
    """
    List all users.
    """

    users = service.list_users()

    return [UserResponse.model_validate(user) for user in users]


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
) -> UserResponse:
    """
    Return the currently authenticated user.
    """

    return UserResponse.model_validate(current_user)


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: UUID,
    service: UserService = Depends(get_user_service),
    _: User = Depends(require_superuser),
) -> UserResponse:
    """
    Retrieve a user by ID.
    """

    user = service.get_user(user_id)

    return UserResponse.model_validate(user)
