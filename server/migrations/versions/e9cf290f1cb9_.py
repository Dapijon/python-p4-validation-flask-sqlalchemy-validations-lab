"""empty message

Revision ID: e9cf290f1cb9
Revises: faa482c1e292
Create Date: 2024-01-13 17:23:11.293832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9cf290f1cb9'
down_revision = 'faa482c1e292'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_author_name', 'authors', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_author_name', 'authors', type_='unique')
    # ### end Alembic commands ###
