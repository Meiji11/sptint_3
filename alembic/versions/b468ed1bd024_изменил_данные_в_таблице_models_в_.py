"""изменил данные в таблице models, в значении os поствил 1, вместо 3

Revision ID: b468ed1bd024
Revises: bd388268bb11
Create Date: 2025-02-07 16:30:46.095180

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b468ed1bd024'
down_revision: Union[str, None] = 'bd388268bb11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
