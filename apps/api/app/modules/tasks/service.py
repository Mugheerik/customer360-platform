import logging

from sqlalchemy.orm import Session

from app.core.exceptions import (
    CustomerNotFoundError,
    TaskNotFoundError,
)
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

logger = logging.getLogger(__name__)


class TaskService:
    """
    Business logic for customer tasks.

    Transaction ownership belongs to the service layer through
    the UnitOfWork.

    A task mutation and its corresponding activity log are treated
    as one atomic business operation. If activity creation fails,
    the task mutation is rolled back as well.
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
        actor_id: str,
    ) -> Task:
        customer = self.customers.get_by_id(
            customer_id,
        )

        if customer is None:
            raise CustomerNotFoundError(
                customer_id,
            )

        logger.info(
            "Creating task for customer '%s'",
            customer_id,
        )

        try:
            created_task = self.tasks.create(
                customer_id,
                task,
            )

            self.activities.create(
                ActivityCreate(
                    entity_type=EntityType.CUSTOMER,
                    entity_id=customer_id,
                    action=ActivityAction.UPDATED,
                    actor_id=actor_id,
                    details={
                        "event": "task_created",
                        "task_id": created_task.id,
                        "title": created_task.title,
                    },
                )
            )

            self.uow.commit()
            self.uow.refresh(created_task)

        except Exception:
            self.uow.rollback()

            logger.exception(
                "Failed to create task for customer '%s'. Transaction rolled back.",
                customer_id,
            )

            raise

        logger.info(
            "Task '%s' created for customer '%s'",
            created_task.id,
            customer_id,
        )

        return created_task

    def get_customer_tasks(
        self,
        customer_id: str,
    ) -> list[Task]:
        customer = self.customers.get_by_id(
            customer_id,
        )

        if customer is None:
            raise CustomerNotFoundError(
                customer_id,
            )

        logger.info(
            "Fetching tasks for customer '%s'",
            customer_id,
        )

        return self.tasks.get_customer_tasks(
            customer_id,
        )

    def update_task(
        self,
        customer_id: str,
        task_id: str,
        data: TaskUpdate,
        actor_id: str,
    ) -> Task:
        task = self.tasks.get_by_id_for_customer(
            task_id,
            customer_id,
        )

        if task is None:
            raise TaskNotFoundError(
                task_id,
            )

        logger.info(
            "Updating task '%s' for customer '%s'",
            task_id,
            customer_id,
        )

        try:
            updated_task = self.tasks.update(
                task,
                data,
            )

            self.activities.create(
                ActivityCreate(
                    entity_type=EntityType.CUSTOMER,
                    entity_id=customer_id,
                    action=ActivityAction.UPDATED,
                    actor_id=actor_id,
                    details={
                        "event": "task_updated",
                        "task_id": updated_task.id,
                        "title": updated_task.title,
                    },
                )
            )

            self.uow.commit()
            self.uow.refresh(updated_task)

        except Exception:
            self.uow.rollback()

            logger.exception(
                "Failed to update task '%s' for customer '%s'. "
                "Transaction rolled back.",
                task_id,
                customer_id,
            )

            raise

        logger.info(
            "Task '%s' updated successfully",
            task_id,
        )

        return updated_task

    def delete_task(
        self,
        customer_id: str,
        task_id: str,
        actor_id: str,
    ) -> None:
        task = self.tasks.get_by_id_for_customer(
            task_id,
            customer_id,
        )

        if task is None:
            raise TaskNotFoundError(
                task_id,
            )

        task_title = task.title

        logger.info(
            "Deleting task '%s' for customer '%s'",
            task_id,
            customer_id,
        )

        try:
            self.tasks.delete(
                task,
            )

            self.activities.create(
                ActivityCreate(
                    entity_type=EntityType.CUSTOMER,
                    entity_id=customer_id,
                    action=ActivityAction.UPDATED,
                    actor_id=actor_id,
                    details={
                        "event": "task_deleted",
                        "task_id": task_id,
                        "title": task_title,
                    },
                )
            )

            self.uow.commit()

        except Exception:
            self.uow.rollback()

            logger.exception(
                "Failed to delete task '%s' for customer '%s'. "
                "Transaction rolled back.",
                task_id,
                customer_id,
            )

            raise
