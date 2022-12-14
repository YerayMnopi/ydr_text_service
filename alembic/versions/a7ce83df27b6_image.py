"""image

Revision ID: a7ce83df27b6
Revises: 8e7486db2444
Create Date: 2022-10-06 12:05:20.919928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7ce83df27b6'
down_revision = '8e7486db2444'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('image', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'image')
    # ### end Alembic commands ###
