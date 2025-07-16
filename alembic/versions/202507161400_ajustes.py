"""ajustes: filtros, paginação e tratamento de erro

Revision ID: 202507161400
Revises: c006e8463eb4
Create Date: 2025-07-16 18:55:37.556

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '202507161400'
down_revision = 'c006e8463eb4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Marcação de versão: filtros, paginação e tratamento de erro adicionados
    pass


def downgrade() -> None:
    # Nenhuma reversão necessária
    pass
