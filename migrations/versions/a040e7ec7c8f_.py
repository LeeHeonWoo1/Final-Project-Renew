"""empty message

Revision ID: a040e7ec7c8f
Revises: 
Create Date: 2023-04-03 17:27:13.747886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a040e7ec7c8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Dance_dataset',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('singer', sa.VARCHAR(length=500), nullable=False),
    sa.Column('src', sa.VARCHAR(length=500), nullable=False),
    sa.Column('youtube_url', sa.VARCHAR(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Test_dataset',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('singer', sa.VARCHAR(length=500), nullable=False),
    sa.Column('src', sa.VARCHAR(length=500), nullable=False),
    sa.Column('youtube_url', sa.VARCHAR(length=600), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('UserInformation',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=150), nullable=False),
    sa.Column('email', sa.VARCHAR(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UserInformation')
    op.drop_table('Test_dataset')
    op.drop_table('Dance_dataset')
    # ### end Alembic commands ###
