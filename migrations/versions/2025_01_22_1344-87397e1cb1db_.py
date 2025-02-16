"""empty message

Revision ID: 87397e1cb1db
Revises: 328918ddd8a4
Create Date: 2025-01-22 13:44:06.342789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87397e1cb1db'
down_revision: Union[str, None] = '328918ddd8a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('theme', sa.String(), nullable=True))
    op.alter_column(
        'articles', 'preview',
        existing_type=sa.VARCHAR(),
        nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('articles', 'preview',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('articles', 'theme')
    # ### end Alembic commands ###
