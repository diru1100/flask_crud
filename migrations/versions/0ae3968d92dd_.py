"""empty message

Revision ID: 0ae3968d92dd
Revises: b56ce8e9a393
Create Date: 2020-05-11 13:36:45.252273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ae3968d92dd'
down_revision = 'b56ce8e9a393'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.String(length=100), nullable=True))
    op.drop_column('post', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author', sa.VARCHAR(length=50), nullable=True))
    op.drop_column('post', 'title')
    # ### end Alembic commands ###
