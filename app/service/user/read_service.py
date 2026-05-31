from app.repository.user.read_repository import get_all_users, get_user_by_id

# Serviço para buscar todos os usuários
def get_all_users_service(session):
    return get_all_users(session)

# Serviço para buscar um usuário por ID
def get_user_by_id_service(
        session,
        user_id: int
    ):

    return get_user_by_id(session, user_id)
