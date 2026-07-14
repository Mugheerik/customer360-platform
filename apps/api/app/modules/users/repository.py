from sqlalchemy.orm import Session

from app.modules.users.models import User


class UserRepository:
    """
    Repository for user database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by email.
        """
        return self.db.query(User).filter(User.email == email).first()

    def get_by_username(self, username: str) -> User | None:
        """
        Retrieve a user by username.
        """
        return self.db.query(User).filter(User.username == username).first()

    def get_by_id(self, user_id: str) -> User | None:
        """
        Retrieve a user by ID.
        """
        return self.db.query(User).filter(User.id == user_id).first()

    def create(self, user: User) -> User:
        """
        Create a new user.
        """
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
