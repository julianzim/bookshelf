"""test migration

Revision ID: 5bb490ddd026
Revises: 
Create Date: 2024-07-19 17:11:17.223134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bb490ddd026'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String()),
                    sa.Column('short_description', sa.String()),
                    sa.Column('full_description', sa.String()),
                    sa.Column('pud_date', sa.String()),
                    sa.Column('author', sa.String()),
                    sa.Column('image', sa.String()),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('articles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String()),
                    sa.Column('short_description', sa.String()),
                    sa.Column('full_description', sa.String()),
                    sa.Column('created_at', sa.TIMESTAMP()),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('articles')
    # ### end Alembic commands ###
