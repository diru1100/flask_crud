"""empty message

Revision ID: 40afa8443da7
Revises: 2e9461538038
Create Date: 2020-05-11 13:40:01.894761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40afa8443da7'
down_revision = '2e9461538038'
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
