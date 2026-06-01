from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.database.database import get_db

from app.service.user.create_user import create_user_service
from app.service.user.delete_user import delete_user_service
from app.service.auth.login import  login_user
from app.service.auth.current_user import get_current_user

from app.schema.user.create_shema import (
    UserCreate,
    UserCreateResponse
)
from app.schema.user.delete_shema import (
    UserDelete
)
from app.schema.user.auth_schema import (
    UserAuthenticate
)

router = APIRouter()

# POST LOGIN
@router.post("/auth/login/")
async def login(
    user: UserAuthenticate = Depends(UserAuthenticate.as_form),
    db: Session = Depends(get_db)
):  
    authenticated_user = login_user(
        session=db,
        dados=user
    )
    return authenticated_user

# POST USERS 
@router.post("/users/", response_model=UserCreateResponse)
async def create_user(
    user: UserCreate = Depends(UserCreate.as_form),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    payload_email = current_user["sub"]
    new_user = create_user_service(
        session=db,
        dados=user,
        email=payload_email
    )
    return new_user

# DELETE USERS 
@router.delete("/users/", response_model=UserCreateResponse)
async def delete_user(
    user: UserDelete = Depends(UserDelete.as_form),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    delete_user = delete_user_service(
        session=db,
        user_id=user.id,
        #token=current_user
    )

    return delete_user
