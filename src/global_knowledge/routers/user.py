from fastapi import APIRouter, HTTPException, Request, Depends
from typing import Union
from src.global_knowledge.schemas import UserInfo
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.user import UserService

user_router = APIRouter(prefix="/user")

@user_router.post("/signup")
def signup(signup_info: UserInfo, db: Session = Depends(get_db)):
    try:
        user_service = UserService()
        user_service.signup(signup_info, db)
        return {"message": "User created successfully"}
    except Exception as e:
        raise e
    
@user_router.post("/login")
def login(login_info: UserInfo, db: Session = Depends(get_db)):
    try:
        user_service = UserService()
        token = user_service.login(login_info, db)
        return token
    except Exception as e:
        raise e