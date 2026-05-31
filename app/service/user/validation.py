from sqlalchemy.orm import Session
from app.models.user_model import User
from app.utils.security.hash_psw import  hash_password
from app.utils.security.verify_psw import  verify_password
from app.repository.user.read_repository import get_user_by_id
from fastapi import HTTPException, status
# Validação de dados Email do usuário existe no banco de dados
def email_user_exists(session: Session, email: str) -> bool:
    return session.query(User).filter(User.email == email).first() is not None

# Validação de dados Email do usuário existe no banco de dados para outro usuário
def update_same_email(session: Session, email: str, user_id: int) -> bool:
    return session.query(User).filter(User.email == email, User.id != user_id).first() is not None

# Validação de dados Senha do usuário é igual a senha atual no banco de dados
def confirm_password(session: Session, password: str, user_id: int) -> bool:
    user = get_user_by_id(session, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if not verify_password(password, user.password, user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )

    return True

# Validação de dados Senha do usuário é diferente da senha atual no banco de dados
def update_same_password(session: Session, password: str, user_id: int) -> bool:
    user = get_user_by_id(session, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if verify_password(password, user.password, user_id):
        raise ValueError("New password cannot be the same as the current password")
    return True
