import bcrypt
# Encripitar a senha do usuário usando bcrypt
def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    hash_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hash_bytes.decode('utf-8')

                          