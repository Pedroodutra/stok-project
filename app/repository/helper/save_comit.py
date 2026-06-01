from app.service.auth.current_user import get_current_user
from fastapi import Depends

# Helper para salvar as alterações no banco de dados
def _save(session):
    session.commit()


