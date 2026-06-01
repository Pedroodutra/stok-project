from app.models.user_model import User
from app.repository.helper.save_comit import _save
# Esta Função é responsável por deletar (Soft Delete) um usuário do banco de dados pelo ID
def delete_user(
        session,
        user_id: int
        ):
    user = session.get(User, user_id)
    if user:
        user.is_active = False
        _save(session)
    return user