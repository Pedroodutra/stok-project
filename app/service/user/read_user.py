from app.repository.user.read_repository import get_all_users, get_all_users_by_name
from app.utils.validations.val_user import validate_user_is_admin
def read_all_users_service(session, email):
    validate_user_is_admin(session, email)
    return get_all_users(session)

def read_users_by_name_service(session, email, name):
    validate_user_is_admin(session, email)
    return get_all_users_by_name(session, name)