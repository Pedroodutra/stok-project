from sqlalchemy.orm import Session
from app.models.user_model import User
from app.repository.user.read_repository import get_user_by_id
from fastapi import HTTPException, status
from app.utils.validations.val_user import validate_user_exists

# Validação de dados Nome do usuário é igual ao nome atual no banco de dados
def update_same_username(
        session: Session, 
        user_id: int, 
        name: str
    ):
    user = validate_user_exists(
        session, 
        user_id
    )
    if user.name is not None and user.name == name:
        raise ValueError("Username is the same as the current username")
