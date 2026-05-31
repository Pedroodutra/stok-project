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