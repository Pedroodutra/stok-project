from fastapi import HTTPException
from app.utils.validations.verify_psw import verify_password
from app.utils.validations.val_email import validate_email_not_registered, get_user_by_email
from app.utils.validations.val_user import validate_user_is_active
from app.utils.security.auth import create_access_token
from app.schema.user.auth_schema import UserAuthenticate

# Cria um serviço de login para autenticar o usuário e gerar um token de acesso
def login_user(session, dados: UserAuthenticate):
    
    if validate_email_not_registered(session, dados.username) is True:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    if validate_email_not_registered(session, dados.username) is False:
        user_db = get_user_by_email(session, dados.username)
        
        validate_user_is_active(session, dados.username)
        
        if not verify_password(dados.password, user_db.password):
            raise HTTPException(status_code=400, detail="Invalid username or password")
        access_token = create_access_token(data={"sub": user_db.email})
        return {"access_token": access_token, "token_type": "bearer"}

 


