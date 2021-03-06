"""empty message

Revision ID: 2e9461538038
Revises: 0ae3968d92dd
Create Date: 2020-05-11 13:37:35.904237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e9461538038'
down_revision = '0ae3968d92dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author', sa.VARCHAR(length=50), nullable=True))
    # ### end Alembic commands ###
