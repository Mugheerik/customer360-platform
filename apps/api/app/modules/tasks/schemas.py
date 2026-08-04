from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.modules.tasks.enums import (
    TaskPriority,
    TaskStatus,
)


class TaskCreate(BaseModel):
    """
    Payload for creating a task.
    """

    title: str = Field(
        min_length=1,
        max_length=255,
    )

    description: str | None = None

    assigned_to: str | None = None

    priority: TaskPriority = TaskPriority.MEDIUM


class TaskUpdate(BaseModel):
    """
    Payload for updating a task.
    """

    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )

    description: str | None = None

    assigned_to: str | None = None

    status: TaskStatus | None = None

    priority: TaskPriority | None = None


class TaskResponse(BaseModel):
    """
    Response model for tasks.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    customer_id: str

    assigned_to: str | None

    title: str

    description: str | None

    status: TaskStatus

    priority: TaskPriority

    created_at: datetime

    updated_at: datetime
