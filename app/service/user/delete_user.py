from app.repository.user.delete_repository import delete_user
from app.utils.validations.val_user import validate_user_exists

# Função de serviço para deletar um usuário
def delete_user_service(    
        session,
        user_id: int
    ):
    # Validar se o usuário existe
    validate_user_exists(
        session,
        user_id
    )   

    return delete_user(
        session,
        user_id=user_id
    )