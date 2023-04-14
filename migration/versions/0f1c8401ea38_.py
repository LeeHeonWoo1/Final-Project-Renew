"""empty message

Revision ID: 0f1c8401ea38
Revises: 
Create Date: 2023-04-13 21:24:49.571397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f1c8401ea38'
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
    op.create_table('UserInformation',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('nickname', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=150), nullable=False),
    sa.Column('email', sa.VARCHAR(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('nickname'),
    sa.UniqueConstraint('username')
    )
    op.create_table('board',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=500), nullable=False),
    sa.Column('section', sa.VARCHAR(length=50), nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('writer', sa.VARCHAR(length=500), nullable=False),
    sa.Column('write_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Replies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('content', sa.VARCHAR(length=500), nullable=False),
    sa.Column('writer', sa.VARCHAR(length=500), nullable=False),
    sa.Column('write_date', sa.DateTime(), nullable=False),
    sa.Column('video_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['video_id'], ['Dance_dataset.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Replies')
    op.drop_table('board')
    op.drop_table('UserInformation')
    op.drop_table('Dance_dataset')
    # ### end Alembic commands ###