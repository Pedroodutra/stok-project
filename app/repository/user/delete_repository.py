from app.models.user_model import User
from app.repository.helper.save_comit import _save
# Esta Função é responsável por deletar (Soft Delete) um usuário do banco de dados pelo ID
def soft_delete_user(
        session,
        user_id: int,
        email: str,
        ):
    user = session.get(User, user_id)
    if user:
        user.updated_by = email
        user.action_updated = "delete"
        user.is_active = False
        _save(session)
    return user

# Esta Função é responsável por deletar (Delete) um usuário do banco de dados pelo ID
def delete_user(
        session,
        user_id: int,
        ):
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        _save(session)
    return user