"""empty message

Revision ID: 145492490dbd
Revises: 242011f2955e
Create Date: 2020-06-24 13:16:08.951408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '145492490dbd'
down_revision = '242011f2955e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('blog_image', sa.String(length=64), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reply',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reply', sa.String(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('blog_post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_post',
    sa.Column('blog_image', sa.VARCHAR(length=64), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('replies', sa.VARCHAR(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=140), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reply')
    op.drop_table('blogs')
    # ### end Alembic commands ###
