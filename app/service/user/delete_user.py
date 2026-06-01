from app.repository.user.delete_repository import soft_delete_user, delete_user
from app.utils.validations.val_user import validate_user_exists, validate_user_is_admin
from app.repository.helper.auditoria import auditoria_user_delete
# Função de serviço para soft_deletar um usuário
def soft_delete_user_service(    
        session,
        user_id: int,
        email: str
    ):
    # Validar se o usuário existe
    validate_user_exists(
        session,
        user_id
    )
    # Validar se o usuário é administrador
    validate_user_is_admin(
        session,
        email
    )
    auditoria = auditoria_user_delete(
        session,
        email=email
    )

    return soft_delete_user(
        session,
        user_id=user_id,
        email=email
    )

# Função de serviço para deletar um usuário
def delete_user_service(    
        session,
        user_id: int,
        email: str
    ):
    # Validar se o usuário existe
    validate_user_exists(
        session,
        user_id
    )
    validate_user_is_admin(
        session,
        email
    )

    return delete_user(
        session,
        user_id=user_id,

    )