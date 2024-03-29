"""empty message

Revision ID: d80f37334843
Revises: 12778d9a190d
Create Date: 2024-01-18 20:26:36.137352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd80f37334843'
down_revision = '12778d9a190d'
branch_labels = None
depends_on = None


from src import db
from src.accounts.models import Account

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

        # sql_query = text(f"UPDATE account SET password = '123456';")
        # db.session.execute(sql_query)
        # db.session.commit()

        # users = db.session.query(Account).all()
        # for user in users:
        #     user.password = '123456'

        # db.session.commit()

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
