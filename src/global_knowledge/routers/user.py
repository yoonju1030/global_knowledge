from fastapi import APIRouter, Depends
from src.global_knowledge.schemas import UserInfo
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.user import UserService

user_router = APIRouter(prefix="/user")


@user_router.post(
    "/signup",
    summary="회원 가입 엔드포인트", 
    description="가입을 원하는 id와 password 를 각각 user_id 값과 password 값으로 지정하여 요청한다."
)
def signup(signup_info: UserInfo, db: Session = Depends(get_db)):
    try:
        user_service = UserService()
        user_service.signup(signup_info, db)
        return {"message": "User created successfully"}
    except Exception as e:
        raise e


@user_router.post(
    "/login",
    summary="로그인 엔드포인트", 
    description="로그인을 원하는 id와 password 를 각각 user_id 값과 password 값으로 지정하여 요청한다. 로그인이 완료되면 access token이 제공된다."
)
def login(login_info: UserInfo, db: Session = Depends(get_db)):
    try:
        user_service = UserService()
        token = user_service.login(login_info, db)
        return token
    except Exception as e:
        raise e
