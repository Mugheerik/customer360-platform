from uuid import UUID

from app.core.exceptions import UserNotFoundError
from app.core.uow import UnitOfWork
from app.modules.users.models import User


class UserService:
    """
    User service.
    """

    def __init__(
        self,
        uow: UnitOfWork,
    ):
        self.uow = uow
        self.users = uow.users

    def list_users(self) -> list[User]:
        """
        Retrieve all users.
        """

        return self.users.get_all()

    def get_user(
        self,
        user_id: UUID,
    ) -> User:
        """
        Retrieve a user by ID.
        """

        user = self.users.get_by_id(user_id)

        if user is None:
            raise UserNotFoundError("User not found.")

        return user
