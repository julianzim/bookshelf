"""empty message

Revision ID: c1e1fc40f7b4
Revises: e6c56a40aa7e
Create Date: 2025-01-11 16:03:05.186292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1e1fc40f7b4'
down_revision: Union[str, None] = 'e6c56a40aa7e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('summary', sa.String(), nullable=True))
    op.add_column('articles', sa.Column('text', sa.String(), nullable=True))
    op.add_column('articles', sa.Column('preview', sa.String(), nullable=True))
    op.alter_column('articles', 'active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.drop_column('articles', 'full_description')
    op.drop_column('articles', 'short_description')
    op.alter_column('books', 'active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.add_column('articles', sa.Column('short_description', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('articles', sa.Column('full_description', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.alter_column('articles', 'active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_column('articles', 'preview')
    op.drop_column('articles', 'text')
    op.drop_column('articles', 'summary')
    # ### end Alembic commands ###
