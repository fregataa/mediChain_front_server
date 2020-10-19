"""empty message

Revision ID: adcbfb2a65ae
Revises: bfbcee1ddde1
Create Date: 2020-10-18 22:42:19.441711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adcbfb2a65ae'
down_revision = 'bfbcee1ddde1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('patientHash', sa.String(length=200), server_default='1', nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.drop_column('patientHash')

    # ### end Alembic commands ###
