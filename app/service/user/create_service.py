from fastapi import HTTPException, status
from app.repository.user.create_repository import create_user
from app.utils.security.hash_psw import hash_password
from app.schema.user.create_shema import(UserCreate)
from app.service.user.validation import(
    email_user_exists,
    )
# Serviço para criar um novo usuário
def create_user_service(
        session, 
        dados: UserCreate
    ):
    hashed_password = hash_password(dados.password)
    email_exists = email_user_exists(session, dados.email)
    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    user = create_user(
        session,
        name=dados.name,
        email=dados.email,
         # Encripitando a senha do usuário usando bcrypt
        hashed_password=hashed_password
    )
    return user
