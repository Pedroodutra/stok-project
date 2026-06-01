from app.repository.user.create_repository import create_user
from app.utils.validations.val_user import validate_user_exists
from app.utils.validations.val_email import validate_email_not_registered
from app.utils.security.hash_psw import hash_password
from app.schema.user.create_shema import UserCreate
from app.repository.helper.auditoria import auditoria_user_create
from app.service.auth.current_user import get_current_user
from fastapi import Depends
from fastapi import HTTPException

# Função de serviço para criar um novo usuário
def create_user_service(    
        session,
        dados: UserCreate,
        email: str
    ):
    # Validar se o email já está registrado
    if validate_email_not_registered(
        session,
        # não usar get_current_user para obter o email do usuário atual, pois estamos criando um novo usuário e não temos um token de acesso, pegariamos o nosso e cairia na validação de email já registrado, então passamos o email do usuário que queremos criar
        dados.email
    ) is False:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash da senha do usuário
    password_hash = hash_password(dados.password)
    auditoria = auditoria_user_create(
        session,
        email=email
    )
    # Criar o usuário no banco de dados
    user = create_user(
        session,
        dados.name,
        dados.email,
        password_hash,
        created_by=auditoria.created_by,
        updated_by=auditoria.updated_by,
        action_updated=auditoria.action_updated

    )
   

    return user