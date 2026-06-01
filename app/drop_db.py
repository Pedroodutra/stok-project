from app.database.database import SessionLocal
from app.models.user_model import User

session = SessionLocal()

session.query(User).delete()
session.commit()
print("Dados do banco de dados apagados com sucesso!")
session.close()