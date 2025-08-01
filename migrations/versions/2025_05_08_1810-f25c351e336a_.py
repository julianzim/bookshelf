"""empty message

Revision ID: f25c351e336a
Revises: 
Create Date: 2025-05-08 18:10:21.333241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f25c351e336a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('approved', sa.Boolean(), server_default=sa.text('false'), nullable=False))
    op.add_column('reviews', sa.Column('rejection_reason', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'rejection_reason')
    op.drop_column('reviews', 'approved')
    # ### end Alembic commands ###
