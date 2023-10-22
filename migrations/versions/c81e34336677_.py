"""empty message

Revision ID: c81e34336677
Revises: ad2750b43fdd
Create Date: 2023-10-22 19:57:21.367594

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c81e34336677'
down_revision: Union[str, None] = 'ad2750b43fdd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.String(),
               existing_nullable=True,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'date',
               existing_type=sa.String(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###
