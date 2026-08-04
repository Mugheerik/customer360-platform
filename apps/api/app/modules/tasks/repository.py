from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.tasks.models import Task
from app.modules.tasks.schemas import (
    TaskCreate,
    TaskUpdate,
)


class TaskRepository:
    """
    Repository for customer tasks.
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
        db_task = Task(
            customer_id=customer_id,
            assigned_to=task.assigned_to,
            title=task.title,
            description=task.description,
            priority=task.priority,
        )

        self.db.add(db_task)
        self.db.flush()
        self.db.refresh(db_task)

        return db_task

    def get_customer_tasks(
        self,
        customer_id: str,
    ) -> list[Task]:
        statement = (
            select(Task)
            .where(
                Task.customer_id == customer_id,
            )
            .order_by(
                Task.created_at.desc(),
            )
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(
        self,
        task_id: str,
    ) -> Task | None:
        statement = select(Task).where(
            Task.id == task_id,
        )

        return self.db.scalar(statement)

    def update(
        self,
        task: Task,
        data: TaskUpdate,
    ) -> Task:
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
        self.db.refresh(task)

        return task

    def delete(
        self,
        task: Task,
    ) -> None:
        self.db.delete(task)
        self.db.flush()
