from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import JSON, DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.modules.activity.enums import (
    ActivityAction,
    EntityType,
)


class ActivityLog(Base):
    """Audit log entry for system activity."""

    __tablename__ = "activity_logs"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    entity_type: Mapped[EntityType] = mapped_column(
        Enum(
            EntityType,
            name="entity_type",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=False,
    )

    entity_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    action: Mapped[ActivityAction] = mapped_column(
        Enum(
            ActivityAction,
            name="activity_action",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=False,
    )

    actor_id: Mapped[str | None] = mapped_column(
        String(36),
        nullable=True,
    )

    details: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
