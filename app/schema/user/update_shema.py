from pydantic import BaseModel, EmailStr, Field
from datetime import datetime 
# Validação de dados para atualização de usuário 
class UserUpdate(BaseModel):
    name: str 
    email: EmailStr 
    password: str = Field(min_length=6)

# Validação de dados para respostas
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    date_created: datetime

    class Config:
        orm_mode = True