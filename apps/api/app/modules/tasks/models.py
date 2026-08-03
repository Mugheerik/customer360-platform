from datetime import UTC, datetime
from uuid import uuid4

from app.database.base import Base
from app.modules.tasks.enums import (
    TaskPriority,
    TaskStatus,
)
from sqlalchemy import DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Task(Base):
    """
    Customer task.
    """

    __tablename__ = "tasks"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    customer_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey(
            "customers.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    assigned_to: Mapped[str | None] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
        ),
        nullable=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[TaskStatus] = mapped_column(
        Enum(
            TaskStatus,
            values_callable=lambda enum: [item.value for item in enum],
        ),
        default=TaskStatus.TODO,
        nullable=False,
    )

    priority: Mapped[TaskPriority] = mapped_column(
        Enum(
            TaskPriority,
            values_callable=lambda enum: [item.value for item in enum],
        ),
        default=TaskPriority.MEDIUM,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )
