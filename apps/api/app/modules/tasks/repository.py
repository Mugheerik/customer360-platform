from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.tasks.models import Task
from app.modules.tasks.schemas import TaskCreate, TaskUpdate


class TaskRepository:
    """
    Repository for customer tasks.

    The repository manages persistence operations only.
    Transaction ownership belongs to the service layer
    through the UnitOfWork.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        customer_id: str,
        task: TaskCreate,
    ) -> Task:
        """
        Stage a new task for persistence.
        """

        db_task = Task(
            customer_id=customer_id,
            assigned_to=task.assigned_to,
            title=task.title,
            description=task.description,
            priority=task.priority,
        )

        self.db.add(db_task)
        self.db.flush()

        return db_task

    def get_customer_tasks(
        self,
        customer_id: str,
    ) -> list[Task]:
        """
        Retrieve all tasks belonging to a customer.
        """

        statement = (
            select(Task)
            .where(
                Task.customer_id == customer_id,
            )
            .order_by(
                Task.created_at.desc(),
            )
        )

        return list(
            self.db.scalars(statement).all(),
        )

    def get_by_id(
        self,
        task_id: str,
    ) -> Task | None:
        """
        Retrieve a task by ID.
        """

        statement = select(Task).where(
            Task.id == task_id,
        )

        return self.db.scalar(statement)

    def get_by_id_for_customer(
        self,
        task_id: str,
        customer_id: str,
    ) -> Task | None:
        """
        Retrieve a task only when it belongs to the
        specified customer.
        """

        statement = select(Task).where(
            Task.id == task_id,
            Task.customer_id == customer_id,
        )

        return self.db.scalar(statement)

    def update(
        self,
        task: Task,
        data: TaskUpdate,
    ) -> Task:
        """
        Apply updates to a task and stage the changes.
        """

        updates = data.model_dump(
            exclude_unset=True,
        )

        for field, value in updates.items():
            setattr(
                task,
                field,
                value,
            )

        self.db.flush()

        return task

    def delete(
        self,
        task: Task,
    ) -> None:
        """
        Stage a task deletion.
        """

        self.db.delete(task)
        self.db.flush()
