"""empty message

Revision ID: 93fdba83a19a
Revises: bf5e87c0b368
Create Date: 2025-01-22 16:22:31.939410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93fdba83a19a'
down_revision: Union[str, None] = 'bf5e87c0b368'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('themes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'articles', 'themes', ['theme'], ['id'], ondelete='CASCADE')
    op.add_column('books', sa.Column('theme', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'books', 'themes', ['theme'], ['id'], ondelete='CASCADE')
    op.drop_column('books', 'mean_rating')
    op.drop_column('books', 'ratings_count')
    op.drop_column('books', 'reviews_count')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('reviews_count', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('books', sa.Column('ratings_count', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('books', sa.Column('mean_rating', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'theme')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_table('themes')
    # ### end Alembic commands ###
