from pydantic import BaseModel, EmailStr
# Validação de dados para resposta de busca de usuário
class UserReadResponse(BaseModel):
    id: int 
    name: str
    email: EmailStr
    created_by: str
    updated_by: str
    action_updated: str
    is_active: bool
    class Config:
        orm_mode = True




