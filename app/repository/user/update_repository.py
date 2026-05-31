from app.models.user_model import User
def update_user(
        session, 
        user_id: int,       
        name: str, 
        email: str, 
        hashed_password: str,
        is_admin: bool = False,
        group_id: int = 2
    ):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")

    user.name = name
    user.email = email
    user.password = hashed_password
    user.is_admin = is_admin
    user.group_id = group_id

    session.add(user)
    session.commit()
    session.refresh(user)
    return user