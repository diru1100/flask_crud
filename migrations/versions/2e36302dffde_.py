"""empty message

Revision ID: 2e36302dffde
Revises: 40afa8443da7
Create Date: 2020-05-11 13:43:56.965234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e36302dffde'
down_revision = '40afa8443da7'
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
