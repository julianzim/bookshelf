"""empty message

Revision ID: e8793ab8dba0
Revises: 3163fc8041b1
Create Date: 2025-06-13 18:40:36.465514

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8793ab8dba0'
down_revision: Union[str, None] = '3163fc8041b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('aloud_link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'aloud_link')
    # ### end Alembic commands ###
