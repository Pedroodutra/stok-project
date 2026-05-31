from app.repository.user.delete_repository import delete_user
from app.service.user.validation import(
    get_user_by_id
    )
# Serviço para deletar um usuário existente
def delete_user_service(
        session,
        user_id: int
    ):

    return delete_user(
        session,
        user_id=user_id
    )
