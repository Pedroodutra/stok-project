from fastapi import Form
from pydantic import BaseModel, EmailStr, Field
# Validação de dados para criação de usuário request

class UserCreate(BaseModel):
    name: str =  Field(min_length=1)
    email: EmailStr 
    password: str = Field(min_length=6)
    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        email: str = Form(...),
        password: str = Form(...)
    ):
        return cls(
            name=name,
            email=email,
            password=password
        )


# Validação de dados para resposta de criação de usuário
class UserCreateResponse(BaseModel):
    id: int 
    name: str
    email: EmailStr



