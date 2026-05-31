from app.models.user_model import User
def delete_user(
        session,
        user_id: int
        ):
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
    return user