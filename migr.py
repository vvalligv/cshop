# In the migrations folder, check the latest migration script, e.g., versions/<some_hash>_add_points_column.py
from alembic import op # type: ignore
import sqlalchemy as sa # type: ignore

# revision identifiers, used by Alembic.
revision = 'some_hash'
down_revision = 'previous_hash'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('user', sa.Column('loyalty_points', sa.Float(), nullable=True, server_default="0.0"))

def downgrade():
    op.drop_column('user', 'loyalty_points')
