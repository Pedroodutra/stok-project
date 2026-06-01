from sqlalchemy.orm import Session
from app.models.user_model import User
from app.repository.user.read_repository import get_user_by_id, get_user_by_email
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

def validate_user_is_admin(
    session: Session,
    email: str
) -> User:
    user = get_user_by_email(
        session,
        email
    )
    if not user or not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not have permission to perform this action"
        )

    return user
def validate_user_is_active(
    session: Session,
    email: str
) -> User:
    user = get_user_by_email(
        session,
        email
    )
    if not user or not user.is_active:
        raise HTTPException(
            status_code=400,
            detail="Email or password is invalid"
        )

    return user

