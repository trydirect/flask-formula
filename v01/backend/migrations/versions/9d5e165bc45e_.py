"""empty message

Revision ID: 9d5e165bc45e
Revises: ce716beab747
Create Date: 2018-01-02 02:51:09.155384

"""
from alembic import op
import sqlalchemy as sa
from hashlib import md5


# revision identifiers, used by Alembic.
revision = '9d5e165bc45e'
down_revision = 'ce716beab747'
branch_labels = None
depends_on = None


def upgrade():
    password = md5('test12345'.encode('utf-8')).hexdigest()
    sql = """INSERT INTO public."users" ("id", "created", "updated", "email", "password", "auth_token") VALUES (1, NOW(), NOW(), 'admin@app.com', '{}', '');""".format(password)
    op.execute(sql)


def downgrade():
    pass
