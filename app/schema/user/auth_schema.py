from fastapi import Form
from pydantic import BaseModel, EmailStr, Field
# Validação de dados para autenticação de usuário request

class UserAuthenticate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    @classmethod
    def as_form(
        cls,
        email: str = Form(""),
        password: str = Form("")
    ):
        return cls(
            email=email,
            password=password
        )