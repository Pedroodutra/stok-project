from sqlalchemy.orm import Session
from app.models.user_model import User
from app.repository.user.read_repository import get_user_by_id
from fastapi import HTTPException, status

# Validação de dados usuario existe no banco de dados
def validate_user_exists(
    session: Session,
    user_id: int
) -> User:
    user = get_user_by_id(
        session,
        user_id
    )
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user
