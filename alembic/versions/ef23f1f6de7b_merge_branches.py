"""Merge branches

Revision ID: ef23f1f6de7b
Revises: add_shipment_tables, f552da6b84e4
Create Date: 2025-05-06 02:14:04.195956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef23f1f6de7b'
down_revision = ('add_shipment_tables', 'f552da6b84e4')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
