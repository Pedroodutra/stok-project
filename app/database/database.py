from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
# 1. Criando a SQLAlchemy engine 
# (conexão com o banco de dados)
DATABASE_URL = "sqlite:///./.database.db"
engine = create_engine(DATABASE_URL)

# 2. Criando a sessao de banco de dados
SessionLocal = sessionmaker(bind=engine)

# 3. Criando a base declarativa para os modelos
class Base(DeclarativeBase):
    pass