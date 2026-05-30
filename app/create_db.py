from app.database import engine, Base
from app.models.user_model import User

# Criando o banco de dados
Base.metadata.create_all(bind=engine)
print("Banco criado!")