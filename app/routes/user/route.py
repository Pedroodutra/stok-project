from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.database.database import get_db
from app.service.user.create_service import create_user_service
from app.service.user.auth_service import  authenticate_user_service
from app.schema.user.create_shema import (
    UserCreate,
    UserCreateResponse
)
from app.schema.user.auth_schema import (
    UserAuthenticate
)

router = APIRouter()
# POST LOGIN
@router.post("/login/")
async def login(
    user: UserAuthenticate = Depends(UserAuthenticate.as_form),
    db: Session = Depends(get_db)
):  
    authenticated_user = authenticate_user_service(
        session=db,
        email=user.email,
        password=user.password
    )
    return authenticated_user

# POST USERS 
@router.post("/users/", response_model=UserCreateResponse)
async def create_user(
    user: UserCreate = Depends(UserCreate.as_form),
    db: Session = Depends(get_db)
):
    new_user = create_user_service(
        session=db,
        dados=user
    )

    return new_user
