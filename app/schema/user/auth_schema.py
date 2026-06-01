from fastapi import Form
from pydantic import BaseModel, EmailStr, Field
# Validação de dados para autenticação de usuário request

class UserAuthenticate(BaseModel):
    username: EmailStr
    password: str = Field(min_length=6)
    @classmethod
    def as_form(
        cls,
        username: EmailStr = Form(...),
        password: str = Form(...)
    ):
        return cls(
            username=username,
            password=password
        )