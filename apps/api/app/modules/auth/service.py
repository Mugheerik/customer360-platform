from app.core.exceptions import ConflictError
from app.core.security.password import hash_password
from app.modules.auth.schemas import RegisterRequest
from app.modules.users.models import User
from app.modules.users.repository import UserRepository


class AuthService:
    """
    Authentication service.
    """

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, request: RegisterRequest) -> User:
        """
        Register a new user.
        """

        existing_user = self.repository.get_by_email(request.email)

        if existing_user:
            raise ConflictError("Email is already registered.")

        existing_user = self.repository.get_by_username(request.username)

        if existing_user:
            raise ConflictError("Username is already taken.")

        user = User(
            email=request.email,
            username=request.username,
            password_hash=hash_password(request.password),
            first_name=request.first_name,
            last_name=request.last_name,
        )

        return self.repository.create(user)
