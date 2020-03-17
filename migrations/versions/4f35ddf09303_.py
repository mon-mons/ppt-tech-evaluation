"""empty message

Revision ID: 4f35ddf09303
Revises: 9ddb31c5faa1
Create Date: 2020-03-16 21:12:01.188647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f35ddf09303'
down_revision = '9ddb31c5faa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('address1', sa.String(length=80), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.Column('telephone_no', sa.String(length=20), nullable=True),
    sa.Column('role', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('addresslocation', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_profiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('biography', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('profilepic', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('created_on', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_profiles_pkey')
    )
    op.drop_table('workers')
    # ### end Alembic commands ###