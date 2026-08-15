"""initial Customer360 schema

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-08-15
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "0001_initial_schema"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Create the initial Customer360 database schema."""

    # ------------------------------------------------------------------
    # PostgreSQL ENUM types
    # ------------------------------------------------------------------

    entity_type = postgresql.ENUM(
        "customer",
        "user",
        name="entity_type",
        create_type=False,
    )

    activity_action = postgresql.ENUM(
        "created",
        "updated",
        "deactivated",
        "activated",
        name="activity_action",
        create_type=False,
    )

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

    bind = op.get_bind()

    entity_type.create(bind, checkfirst=True)
    activity_action.create(bind, checkfirst=True)
    task_status.create(bind, checkfirst=True)
    task_priority.create(bind, checkfirst=True)

    # ------------------------------------------------------------------
    # Customers
    # ------------------------------------------------------------------

    op.create_table(
        "customers",
        sa.Column(
            "id",
            sa.String(length=36),
            nullable=False,
        ),
        sa.Column(
            "first_name",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "last_name",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "email",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "phone",
            sa.String(length=30),
            nullable=True,
        ),
        sa.Column(
            "status",
            sa.String(length=30),
            nullable=False,
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
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )

    # ------------------------------------------------------------------
    # Users
    # ------------------------------------------------------------------

    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "email",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "username",
            sa.String(length=50),
            nullable=False,
        ),
        sa.Column(
            "password_hash",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "first_name",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "last_name",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),
        sa.Column(
            "is_superuser",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
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
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_users_email",
        "users",
        ["email"],
        unique=True,
    )

    op.create_index(
        "ix_users_username",
        "users",
        ["username"],
        unique=True,
    )

    # ------------------------------------------------------------------
    # Activity logs
    # ------------------------------------------------------------------

    op.create_table(
        "activity_logs",
        sa.Column(
            "id",
            sa.String(length=36),
            nullable=False,
        ),
        sa.Column(
            "entity_type",
            entity_type,
            nullable=False,
        ),
        sa.Column(
            "entity_id",
            sa.String(length=36),
            nullable=False,
        ),
        sa.Column(
            "action",
            activity_action,
            nullable=False,
        ),
        sa.Column(
            "actor_id",
            sa.String(length=36),
            nullable=True,
        ),
        sa.Column(
            "details",
            sa.JSON(),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    # ------------------------------------------------------------------
    # Notes
    # ------------------------------------------------------------------

    op.create_table(
        "notes",
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
            "author_id",
            sa.UUID(),
            nullable=True,
        ),
        sa.Column(
            "content",
            sa.Text(),
            nullable=False,
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
            ["author_id"],
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

    # ------------------------------------------------------------------
    # Tasks
    # ------------------------------------------------------------------

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
    """Drop the initial Customer360 database schema."""

    bind = op.get_bind()

    op.drop_table("tasks")
    op.drop_table("notes")
    op.drop_table("activity_logs")

    op.drop_index(
        "ix_users_username",
        table_name="users",
    )
    op.drop_index(
        "ix_users_email",
        table_name="users",
    )

    op.drop_table("users")
    op.drop_table("customers")

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

    activity_action = postgresql.ENUM(
        "created",
        "updated",
        "deactivated",
        "activated",
        name="activity_action",
        create_type=False,
    )

    entity_type = postgresql.ENUM(
        "customer",
        "user",
        name="entity_type",
        create_type=False,
    )

    task_priority.drop(bind, checkfirst=True)
    task_status.drop(bind, checkfirst=True)
    activity_action.drop(bind, checkfirst=True)
    entity_type.drop(bind, checkfirst=True)
