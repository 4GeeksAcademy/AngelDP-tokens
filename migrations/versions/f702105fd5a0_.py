"""empty message

Revision ID: f702105fd5a0
Revises: 5f0cbf0b387b
Create Date: 2025-03-24 14:51:30.414547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f702105fd5a0'
down_revision = '5f0cbf0b387b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
        batch_op.drop_column('is_active')
        batch_op.drop_column('password')

    # ### end Alembic commands ###
