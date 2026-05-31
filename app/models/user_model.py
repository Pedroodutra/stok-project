from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base

# Criando o modelo de usuário ORM Classe 
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        autoincrement=True
        )
    name: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
        )
    email: Mapped[str] = mapped_column(
        String(255), 
        unique=True, 
        nullable=False
        )
    password: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
        ) 
    date_created: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.utcnow
        )
    is_admin: Mapped[bool] = mapped_column(
        default=False
    )
    group_id: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )