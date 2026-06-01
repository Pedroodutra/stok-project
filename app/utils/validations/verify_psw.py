import bcrypt
def verify_password(
    password: str,
    password_hash: str
):

    return bcrypt.checkpw(
        password.encode(),
        password_hash.encode()
    )