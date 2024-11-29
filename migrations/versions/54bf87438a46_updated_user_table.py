"""Updated User Table

Revision ID: 54bf87438a46
Revises: 07c503ad2b3c
Create Date: 2024-11-29 20:13:07.176628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54bf87438a46'
down_revision = '07c503ad2b3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('role_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('role_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###