from uuid import UUID

from app.core.exceptions import CustomerNotFoundError
from app.modules.users.models import User
from app.modules.users.repository import UserRepository


class UserService:
    """
    User service.
    """

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def list_users(self) -> list[User]:
        """
        Retrieve all users.
        """

        return self.repository.get_all()

    def get_user(self, user_id: UUID) -> User:
        """
        Retrieve a user by ID.
        """

        user = self.repository.get_by_id(user_id)

        if user is None:
            raise CustomerNotFoundError("User not found.")

        return user
