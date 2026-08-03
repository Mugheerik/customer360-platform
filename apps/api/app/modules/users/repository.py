from uuid import UUID

from app.modules.users.models import User
from sqlalchemy.orm import Session


class UserRepository:
    """
    Repository for user database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        """
        Retrieve a user by email.
        """
        return self.db.query(User).filter(User.email == email).first()

    def get_by_username(
        self,
        username: str,
    ) -> User | None:
        """
        Retrieve a user by username.
        """
        return self.db.query(User).filter(User.username == username).first()

    def get_by_id(
        self,
        user_id: UUID,
    ) -> User | None:
        """
        Retrieve a user by ID.
        """
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all(self) -> list[User]:
        """
        Retrieve all users.
        """
        return self.db.query(User).all()

    def create(
        self,
        user: User,
    ) -> User:
        """
        Stage a new user for persistence.

        Transaction management is handled by the
        application service / Unit of Work.
        """
        self.db.add(user)

        return user
