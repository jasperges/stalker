"""added html_style and html_class columns to SimpleEntities

Revision ID: 5168cc8552a3
Revises: 174567b9c159
Create Date: 2013-11-14 23:03:55.413681

"""

# revision identifiers, used by Alembic.
revision = '5168cc8552a3'
down_revision = '174567b9c159'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('SimpleEntities', sa.Column('html_class', sa.String(), nullable=True))
    op.add_column('SimpleEntities', sa.Column('html_style', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('SimpleEntities', 'html_style')
    op.drop_column('SimpleEntities', 'html_class')
    ### end Alembic commands ###
