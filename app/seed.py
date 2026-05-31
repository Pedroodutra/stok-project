from app.database.database import SessionLocal
from app.models.user_model import User
from app.utils.security.security import hash_password

db = SessionLocal()

try:
    admin = db.query(User).filter(
        User.email == "admin@email.com"
    ).first()

    if not admin:
        db.add(
            User(
                name="Administrador",
                email="admin@email.com",
                password=hash_password("123456"),
                is_admin=True,
                group_id=1
            )
        )
        db.commit()
        print("Usuário admin criado com sucesso!")

finally:
    db.close()