from app.repository.user.update_repository import update_user
from app.utils.security.hash_psw import hash_password
from app.schema.user.update_shema import UserUpdate
 

# Serviço para atualizar os dados de um usuário existente
def update_user_service(
        session, 
        user_id: int, 
        dados: UserUpdate
    ):

    hashed_password = hash_password(dados.password)

    return update_user(
        session,
        user_id=user_id,
        name=dados.name,
        email=dados.email,
        hashed_password=hashed_password
    )
