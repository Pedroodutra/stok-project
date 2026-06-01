from sqlalchemy.orm import Session
from app.repository.user.read_repository import get_user_by_email
from fastapi import HTTPException, status
 


# Validação de dados Email do usuário existe no banco de dados para outro usuário
def validate_email_not_registered(
    session: Session,
    email: str
    ) -> bool:  
    user = get_user_by_email(
        session,
        email
    )
    if user:
        # Email já registrado para outro usuário
        return False
    
    return True
# Validação de dados Email do usuário existe no banco de dados para outro usuário
def update_same_email(
        session: Session, 
        email: str
    ):
    user = get_user_by_email(session, email)
    if user is not None:
        if user.email is not None and user.email == email:
            raise HTTPException(
                status_code=404,
                detail="Email is the same as the current email"
            )
