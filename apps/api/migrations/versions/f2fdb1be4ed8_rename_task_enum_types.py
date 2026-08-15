"""rename task enum types

Revision ID: f2fdb1be4ed8
Revises: b64306b05a1a
Create Date: 2026-08-13 09:47:50.343104
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "f2fdb1be4ed8"
down_revision: Union[str, Sequence[str], None] = "b64306b05a1a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Rename task enum types to match the application model."""

    op.execute(
        "ALTER TYPE taskstatus RENAME TO task_status",
    )

    op.execute(
        "ALTER TYPE taskpriority RENAME TO task_priority",
    )


def downgrade() -> None:
    """Restore the previous task enum type names."""

    op.execute(
        "ALTER TYPE task_status RENAME TO taskstatus",
    )

    op.execute(
        "ALTER TYPE task_priority RENAME TO taskpriority",
    )