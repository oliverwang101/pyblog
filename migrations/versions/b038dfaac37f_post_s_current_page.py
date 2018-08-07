"""post's current page

Revision ID: b038dfaac37f
Revises: c051007a1024
Create Date: 2018-07-18 10:39:44.816166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b038dfaac37f'
down_revision = 'c051007a1024'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('curr_page', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'curr_page')
    # ### end Alembic commands ###
