"""add tasks table

Revision ID: f2fdb1be4ed8
Revises: b64306b05a1a
Create Date: 2026-08-13 09:47:50.343104
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


revision: str = "f2fdb1be4ed8"
down_revision: Union[str, Sequence[str], None] = "b64306b05a1a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    bind = op.get_bind()

    task_status = postgresql.ENUM(
        "todo",
        "in_progress",
        "done",
        name="task_status",
        create_type=False,
    )

    task_priority = postgresql.ENUM(
        "low",
        "medium",
        "high",
        name="task_priority",
        create_type=False,
    )

    task_status.create(bind, checkfirst=True)
    task_priority.create(bind, checkfirst=True)

    op.create_table(
        "tasks",
        sa.Column(
            "id",
            sa.String(length=36),
            nullable=False,
        ),
        sa.Column(
            "customer_id",
            sa.String(length=36),
            nullable=False,
        ),
        sa.Column(
            "assigned_to",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "title",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "status",
            task_status,
            nullable=False,
            server_default="todo",
        ),
        sa.Column(
            "priority",
            task_priority,
            nullable=False,
            server_default="medium",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["assigned_to"],
            ["users.id"],
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["customer_id"],
            ["customers.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""

    bind = op.get_bind()

    op.drop_table("tasks")

    task_priority = postgresql.ENUM(
        "low",
        "medium",
        "high",
        name="task_priority",
        create_type=False,
    )

    task_status = postgresql.ENUM(
        "todo",
        "in_progress",
        "done",
        name="task_status",
        create_type=False,
    )

    task_priority.drop(bind, checkfirst=True)
    task_status.drop(bind, checkfirst=True)