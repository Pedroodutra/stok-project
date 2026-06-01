from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Boolean
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
    created_by: Mapped[str] = mapped_column(
        String(255),
        nullable=True
        )
    date_created: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.utcnow
        )
    updated_by: Mapped[str] = mapped_column(
        String(255),
        nullable=True
        )
    date_updated: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
        )
    action_updated: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )
    is_active = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    is_admin: Mapped[bool] = mapped_column(
        default=False
    )
    group_id: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )
