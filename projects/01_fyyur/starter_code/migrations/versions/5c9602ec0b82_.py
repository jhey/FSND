"""empty message

Revision ID: 5c9602ec0b82
Revises: 9a9e1b8507f8
Create Date: 2019-12-28 13:09:21.135811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c9602ec0b82'
down_revision = '9a9e1b8507f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('venue_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'venue_name')
    # ### end Alembic commands ###
