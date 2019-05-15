"""empty message

Revision ID: ce716beab747
Revises: 
Create Date: 2018-01-02 02:37:55.493039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce716beab747'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('updated', sa.DateTime(), nullable=True),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('password', sa.String(length=255), nullable=True),
        sa.Column('auth_token', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(op.f('ix_users__auth_token'), 'users', ['auth_token'], unique=True)


def downgrade():
    op.drop_index(op.f('ix_users__auth_token'), table_name='users')
    op.drop_table('users')
