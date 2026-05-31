from app.models.user_model import User
from app.repository.user.read_repository import get_user_by_id
from app.utils.security.hash_psw import hash_password
from app.utils.security.verify_psw import verify_password
from fastapi import HTTPException, status

# Serviço para autenticar um usuário
def authenticate_user_service(session, email: str, password: str):
    user = session.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect email or password"
        )

    if not verify_password(password, user.password, user.id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return user