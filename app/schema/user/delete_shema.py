from fastapi import Form
from pydantic import BaseModel, EmailStr
# Validação de dados para deleção de usuário request
class UserDelete(BaseModel):
    id: int
    @classmethod
    def as_form(
        cls,
        id: int = Form(...),
    ):
        return cls(
            id=id,
        )