from sqlalchemy.orm import Session

from app.core.exceptions import (
    ConflictError,
    UnauthorizedError,
)
from app.core.security.jwt import create_access_token
from app.core.security.password import (
    hash_password,
    verify_password,
)
from app.core.uow import UnitOfWork
from app.modules.auth.schemas import (
    LoginRequest,
    RegisterRequest,
)
from app.modules.users.models import User


class AuthService:
    """
    Authentication service.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.uow = UnitOfWork(db)
        self.users = self.uow.users

    def register(
        self,
        request: RegisterRequest,
    ) -> User:
        existing_user = self.users.get_by_email(request.email)

        if existing_user:
            raise ConflictError("Email is already registered.")

        existing_user = self.users.get_by_username(request.username)

        if existing_user:
            raise ConflictError("Username is already taken.")

        user = User(
            email=request.email,
            username=request.username,
            password_hash=hash_password(request.password),
            first_name=request.first_name,
            last_name=request.last_name,
        )

        self.users.create(user)

        self.uow.commit()
        self.uow.refresh(user)

        return user

    def login(
        self,
        request: LoginRequest,
    ) -> str:
        user = self.users.get_by_email(request.email)

        if user is None:
            raise UnauthorizedError("Invalid email or password.")

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise UnauthorizedError("Invalid email or password.")

        return create_access_token(str(user.id))
