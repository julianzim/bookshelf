"""empty message

Revision ID: e6c56a40aa7e
Revises: 
Create Date: 2025-01-10 22:59:16.362026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6c56a40aa7e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('books', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'active')
    op.drop_column('articles', 'active')
    # ### end Alembic commands ###
