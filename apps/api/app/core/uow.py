from typing import Any

from sqlalchemy.orm import Session

from app.modules.activity.repository import ActivityRepository
from app.modules.customers.repository import CustomerRepository
from app.modules.notes.repository import NoteRepository
from app.modules.tasks.repository import TaskRepository
from app.modules.users.repository import UserRepository


class UnitOfWork:
    """
    Coordinates repositories and transaction management.

    The UnitOfWork owns the SQLAlchemy session and provides the
    transaction boundary for application service operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

        self.customers = CustomerRepository(db)
        self.users = UserRepository(db)
        self.activities = ActivityRepository(db)
        self.notes = NoteRepository(db)
        self.tasks = TaskRepository(db)

    def commit(self) -> None:
        """
        Commit the current transaction.
        """

        self.db.commit()

    def rollback(self) -> None:
        """
        Roll back the current transaction.
        """

        self.db.rollback()

    def flush(self) -> None:
        """
        Flush pending changes without committing.

        This is useful when a service needs database-generated
        values or needs constraint errors to occur before the
        final transaction commit.
        """

        self.db.flush()

    def refresh(
        self,
        instance: Any,
    ) -> None:
        """
        Refresh an ORM instance from the database.
        """

        self.db.refresh(instance)
