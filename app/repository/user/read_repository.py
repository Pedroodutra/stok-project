from app.models.user_model import User

# Esta Função é responsável por listar todos os usuários do banco de dados
def get_all_users(session):
    return session.query(User).all()

# Esta Função é responsável por buscar um usuário no banco de dados pelo ID
def get_user_by_id(
        session, 
        user_id: int
    ):
    return session.get(
        User, 
        user_id
        )

# Esta Função é responsável por buscar um usuário no banco de dados pelo email
def get_user_by_email(
    session,
    email: str
):
    return (
        session.query(User)
        .filter(User.email == email)
        .first()
    )

# Esta Função é responsável por buscar todos os usuários no banco de dados pelo nome
def get_all_users_by_name(
        session, 
        name: str
    ):
    return session.query(User).filter(User.name == name).all()


