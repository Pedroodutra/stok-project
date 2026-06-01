from app.service.auth.current_user import verify_access_token, get_current_user
from fastapi import Depends
from app.models.user_model import User
from app.repository.helper.save_comit import _save

def auditoria_user_create(
    session,
    email: str
    ):
    user = User(
        created_by=email,
        updated_by=email,
        action_updated="created"
    )
    _save(session)
    return user


def auditoria_user_update(
    session,
    email: str
    ):

     
    user = User(
        updated_by=email,
        action_updated="updated"
    )
    _save(session)
    return user
  
def auditoria_user_delete(
    session,
    email: str
    ):
   
    user = User(
        updated_by=email,
        action_updated="deleted"
    )
    _save(session)
    return user
  
