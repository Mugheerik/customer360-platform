from sqlalchemy.orm import Session

from app.modules.activity.repository import ActivityRepository
from app.modules.customers.repository import CustomerRepository
from app.modules.notes.repository import NoteRepository
from app.modules.tasks.repository import TaskRepository
from app.modules.users.repository import UserRepository


class UnitOfWork:
    """
    Coordinates repositories and transaction management.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

        # Repositories
        self.customers = CustomerRepository(db)
        self.users = UserRepository(db)
        self.activities = ActivityRepository(db)
        self.notes = NoteRepository(db)
        self.tasks = TaskRepository(db)

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def refresh(
        self,
        instance,
    ) -> None:
        self.db.refresh(instance)

    def flush(self) -> None:
        self.db.flush()
