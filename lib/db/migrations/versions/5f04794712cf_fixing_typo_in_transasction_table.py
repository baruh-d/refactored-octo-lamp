"""fixing typo in Transasction table

Revision ID: 5f04794712cf
Revises: eee6f518e61f
Create Date: 2024-03-25 00:52:07.899559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f04794712cf'
down_revision: Union[str, None] = 'eee6f518e61f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('transaction_type', sa.String(length=10), nullable=True))
    op.drop_column('transactions', 'trasaction_type')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('trasaction_type', sa.VARCHAR(length=10), nullable=True))
    op.drop_column('transactions', 'transaction_type')
    # ### end Alembic commands ###
