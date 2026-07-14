from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.auth.schemas import RegisterRequest, RegisterResponse
from app.modules.auth.service import AuthService
from app.modules.users.repository import UserRepository

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=201,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
) -> RegisterResponse:
    """
    Register a new user.
    """

    repository = UserRepository(db)
    service = AuthService(repository)

    user = service.register(request)

    return RegisterResponse.model_validate(user)
