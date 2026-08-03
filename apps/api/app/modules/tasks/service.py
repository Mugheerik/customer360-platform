import logging

from app.core.exceptions import CustomerNotFoundError, TaskNotFoundError
from app.core.uow import UnitOfWork
from app.modules.activity.enums import (
    ActivityAction,
    EntityType,
)
from app.modules.activity.schemas import ActivityCreate
from app.modules.tasks.models import Task
from app.modules.tasks.schemas import (
    TaskCreate,
    TaskUpdate,
)
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


class TaskService:
    """
    Business logic for customer tasks.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.uow = UnitOfWork(db)

        self.tasks = self.uow.tasks
        self.customers = self.uow.customers
        self.activities = self.uow.activities

    def create_task(
        self,
        customer_id: str,
        task: TaskCreate,
    ) -> Task:
        customer = self.customers.get_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundError(customer_id)

        logger.info(
            "Creating task for customer '%s'",
            customer_id,
        )

        created_task = self.tasks.create(
            customer_id,
            task,
        )

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=customer_id,
                action=ActivityAction.UPDATED,
                performed_by=task.assigned_to,
                details={
                    "event": "task_created",
                    "task_id": created_task.id,
                    "title": created_task.title,
                },
            )
        )

        self.uow.commit()
        self.uow.refresh(created_task)

        return created_task

    def get_customer_tasks(
        self,
        customer_id: str,
    ) -> list[Task]:
        customer = self.customers.get_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundError(customer_id)

        return self.tasks.get_customer_tasks(customer_id)

    def update_task(
        self,
        task_id: str,
        data: TaskUpdate,
    ) -> Task:
        task = self.tasks.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        updated_task = self.tasks.update(
            task,
            data,
        )

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=task.customer_id,
                action=ActivityAction.UPDATED,
                performed_by=updated_task.assigned_to,
                details={
                    "event": "task_updated",
                    "task_id": updated_task.id,
                    "title": updated_task.title,
                },
            )
        )

        self.uow.commit()
        self.uow.refresh(updated_task)

        return updated_task

    def delete_task(
        self,
        task_id: str,
    ) -> None:
        task = self.tasks.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        customer_id = task.customer_id
        task_title = task.title

        self.tasks.delete(task)

        self.activities.create(
            ActivityCreate(
                entity_type=EntityType.CUSTOMER,
                entity_id=customer_id,
                action=ActivityAction.UPDATED,
                details={
                    "event": "task_deleted",
                    "task_id": task_id,
                    "title": task_title,
                },
            )
        )

        self.uow.commit()
