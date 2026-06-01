from datetime import datetime
from datetime import timedelta
from datetime import timezone
from app.utils.validations.val_user import get_user_by_id
from jose import jwt, JWTError

# Configurações de segurança para autenticação e geração de tokens JWT
SECRET_KEY = "STOK-SECRET-KEY-1234567890"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


# Função para criar um token de acesso JWT
def create_access_token(
    data: dict
):

    to_encode = data.copy()

    expire = datetime.now(
        timezone.utc
    ) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# Função para verificar e decodificar um token de acesso JWT
def verify_access_token(
    token: str
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        
        return payload
    except JWTError:
        raise JWTError("Invalid token")
        