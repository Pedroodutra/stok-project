from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.database.database import get_session

from app.service.user.create_user import create_user_service
from app.service.user.delete_user import delete_user_service, soft_delete_user_service
from app.service.user.read_user import read_all_users_service, read_users_by_name_service


from app.service.auth.login import  login_user
from app.service.auth.current_user import get_current_user

from app.schema.user.create_shema import ( UserCreate , UserCreateResponse )
from app.schema.user.read_shema import ( UserReadResponse )
from app.schema.user.update_shema import ( UserResponse )
from app.schema.user.delete_shema import ( UserDeleteResponse )

from app.schema.user.delete_shema import (UserDelete)


from app.schema.user.auth_schema import (UserAuthenticate)

router = APIRouter()

# POST LOGIN
@router.post("/auth/login/", tags=["auth"])
async def login(
    user: UserAuthenticate = Depends(UserAuthenticate.as_form),
    session: Session = Depends(get_session)
):  
    authenticated_user = login_user(
        session=session,
        dados=user
    )
    return authenticated_user

# POST USERS 
@router.post("/users/", response_model=UserCreateResponse, tags=["users"])
async def create_user(
    user: UserCreate = Depends(UserCreate.as_form),
    session: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    payload_email = current_user["sub"]
    new_user = create_user_service(
        session=session,
        dados=user,
        email=payload_email
    )
    return new_user
# GET ALL USERS 
@router.get("/admin/users/", response_model=list[UserReadResponse], tags=["admin"])
async def read_all_users(
    session: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    playload_email = current_user["sub"]
    users = read_all_users_service(session, playload_email)
    return users

# GET ALL USERS BY NAME
@router.get("/admin/users/{name}", tags=["admin"])
async def read_users_by_name(
    name: str,
    session: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    playload_email = current_user["sub"]
    users = read_users_by_name_service(session, playload_email, name)
    return users

# DELETE USERS 
@router.delete("/admin/users/", response_model=UserDeleteResponse, tags=["admin"])
async def delete_user(
    user: UserDelete = Depends(UserDelete.as_form),
    session: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):  

    playload_email = current_user["sub"]
    delete_user = delete_user_service( 
        session=session,
        user_id=user.id,
        email = playload_email
    )

    return delete_user

# SOFT DELETE USERS 
@router.delete("/users/", response_model=UserDeleteResponse, tags=["users"])
async def soft_delete_user(
    user: UserDelete = Depends(UserDelete.as_form),
    session: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    payload_email = current_user["sub"]
    delete_user = soft_delete_user_service(
        session=session,
        user_id=user.id,
        email=payload_email
    )

    return delete_user
