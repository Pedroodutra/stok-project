from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.utils.security.auth import verify_access_token

# Serviço para obter o usuário atual a partir do token de acesso
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)  

# Função para obter o usuário atual a partir do token de acesso
def get_current_user(
    token: str = Depends(oauth2_scheme)
    ):
    playload = verify_access_token(token)
    
    if not playload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return playload