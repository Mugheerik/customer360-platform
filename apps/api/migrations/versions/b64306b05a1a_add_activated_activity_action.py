"""add activated activity action

Revision ID: b64306b05a1a
Revises: 33590051d981
Create Date: 2026-08-09 10:54:58.192632

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "b64306b05a1a"
down_revision: Union[str, Sequence[str], None] = "33590051d981"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.execute(
        "ALTER TYPE activity_action ADD VALUE IF NOT EXISTS 'activated'"
    )


def downgrade() -> None:
    """Downgrade schema."""

    pass