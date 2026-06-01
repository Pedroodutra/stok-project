from app.database.database import SessionLocal
from app.models.user_model import User
from app.utils.security.hash_psw import hash_password

session = SessionLocal()

try:
    admin = session.query(User).filter(
        User.email == "admin@email.com"
    ).first()

    if not admin:
        session.add(
            User(
                name="admin",
                email="admin@email.com",
                password=hash_password("123456"),
                created_by="admin@email.com",
                updated_by="admin@email.com",
                action_updated="create",
                is_admin=True,
                group_id=1
            )
        )
        session.commit()
        print("Usuário admin criado com sucesso!")

finally:
    session.close()