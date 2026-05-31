import bcrypt

# Desencriptar a senha do usuário usando bcrypt
def verify_password(password: str, hashed_password: str, user_id: int) -> bool:
    password_bytes = password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)