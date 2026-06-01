from app.models.user_model import User
from app.repository.helper.save_comit import _save
# Função ORM para manipulação dos dados de usuário
# Esta Função é responsável por criar um novo usuário no banco de dados, utilizando os dados fornecidos e a senha encriptada.
def create_user(
        session, 
        name: str, 
        email: str, 
        hashed_password: str,
        updated_by: str,
        action_updated: str,
        created_by: str,
        is_admin: bool = False,
        group_id: int = 2

    ):

  
    user = User(
        name=name,
        email=email,
        password=hashed_password,
        is_admin=is_admin,
        group_id=group_id,
        created_by=created_by,
        updated_by=updated_by,
        action_updated=action_updated
    )
    session.add(user)
    _save(session)
    session.refresh(user)
    return user