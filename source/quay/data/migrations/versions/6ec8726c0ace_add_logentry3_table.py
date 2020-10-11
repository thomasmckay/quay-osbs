"""
Add LogEntry3 table.

Revision ID: 6ec8726c0ace
Revises: 54492a68a3cf
Create Date: 2019-01-03 13:41:02.897957
"""

# revision identifiers, used by Alembic.
revision = "6ec8726c0ace"
down_revision = "54492a68a3cf"

import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade(op, tables, tester):
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "logentry3",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("kind_id", sa.Integer(), nullable=False),
        sa.Column("account_id", sa.Integer(), nullable=False),
        sa.Column("performer_id", sa.Integer(), nullable=True),
        sa.Column("repository_id", sa.Integer(), nullable=True),
        sa.Column("datetime", sa.DateTime(), nullable=False),
        sa.Column("ip", sa.String(length=255), nullable=True),
        sa.Column("metadata_json", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_logentry3")),
    )
    op.create_index(
        "logentry3_account_id_datetime", "logentry3", ["account_id", "datetime"], unique=False
    )
    op.create_index("logentry3_datetime", "logentry3", ["datetime"], unique=False)
    op.create_index(
        "logentry3_performer_id_datetime", "logentry3", ["performer_id", "datetime"], unique=False
    )
    op.create_index(
        "logentry3_repository_id_datetime_kind_id",
        "logentry3",
        ["repository_id", "datetime", "kind_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade(op, tables, tester):
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("logentry3")
    # ### end Alembic commands ###