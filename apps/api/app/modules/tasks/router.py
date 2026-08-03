from app.database.dependencies import get_db
from app.modules.tasks.schemas import (
    TaskCreate,
    TaskResponse,
    TaskUpdate,
)
from app.modules.tasks.service import TaskService
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/customers/{customer_id}/tasks",
    tags=["Tasks"],
)


def get_task_service(
    db: Session = Depends(get_db),
) -> TaskService:
    return TaskService(db)


@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    customer_id: str,
    task: TaskCreate,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    created_task = service.create_task(
        customer_id,
        task,
    )

    return TaskResponse.model_validate(created_task)


@router.get(
    "",
    response_model=list[TaskResponse],
)
def get_customer_tasks(
    customer_id: str,
    service: TaskService = Depends(get_task_service),
) -> list[TaskResponse]:
    tasks = service.get_customer_tasks(customer_id)

    return [TaskResponse.model_validate(task) for task in tasks]


@router.patch(
    "/{task_id}",
    response_model=TaskResponse,
)
def update_task(
    customer_id: str,
    task_id: str,
    task: TaskUpdate,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    updated_task = service.update_task(
        task_id,
        task,
    )

    return TaskResponse.model_validate(updated_task)


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    customer_id: str,
    task_id: str,
    service: TaskService = Depends(get_task_service),
) -> None:
    service.delete_task(task_id)
