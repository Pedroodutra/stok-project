from app.models.user_model import User

# Função ORM para manipulação dos dados de usuário
# Esta Função é responsável por criar um novo usuário no banco de dados, utilizando os dados fornecidos e a senha encriptada.
def create_user(
        session, 
        name: str, 
        email: str, 
        hashed_password: str,
        is_admin: bool = False,
        group_id: int = 2
    ):
  
    user = User(
        name=name,
        email=email,
        password=hashed_password,
        is_admin=is_admin,
        group_id=group_id
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user