from app.models.user_model import User
from app.repository.user.read_repository import get_user_by_id

# Função atualizar o nome de um usuário existente no banco de dados
def update_user_name(
        session,
        user_id,
        name                
    ):
    user = get_user_by_id(session, user_id)
   
    
    user.name = name
    session.commit()
    session.refresh(user)
    
    return user

# Função atualizar o email de um usuário existente no banco de dados
def update_user_email(
        session,
        user_id,
        email
    ):
    user = get_user_by_id(session, user_id)
    if not user:
        return None
    
    user.email = email
    session.commit()
    session.refresh(user)
    
    return user

# Função atualizar o password de um usuário existente no banco de dados
def update_password(
        session,
        user_id,
        password_hash   
    ):
    user = get_user_by_id(session, user_id)
    if not user:
        return None
    
    user.password_hash = password_hash
    session.commit()
    session.refresh(user)
    
    return user
