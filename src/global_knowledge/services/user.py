from sqlalchemy.orm import Session
from src.global_knowledge.models import User
from src.global_knowledge.schemas import UserInfo
from fastapi import HTTPException
from src.global_knowledge.auth import hash_password, verify_password, create_access_token
from uuid import UUID, uuid4
from datetime import datetime, timedelta

class UserService:
    def __init__(self):
        pass

    def signup(self, signup_info: UserInfo ,db: Session):
        try:
            db_user = db.query(User).filter(User.user_id == signup_info.user_id).first()
            if db_user:
                raise HTTPException(status_code=400, detail="User id already exists")
            
            hashed_password = hash_password(signup_info.password)
            new_user = User(id=str(uuid4()),user_id=signup_info.user_id, hashed_password=hashed_password, admin_status=False)
            
            db.add(new_user)
            db.commit()
        except Exception as e:
            raise e
        
    def login(self, login_info: UserInfo, db: Session):
        try:
            db_user = db.query(User).filter(User.user_id == login_info.user_id).first()
            if not db_user or not verify_password(login_info.password, db_user.hashed_password):
                raise HTTPException(status_code=400, detail="Invalid credentials")

            access_token = create_access_token(data={"sub": db_user.user_id}, expires_delta=timedelta(minutes=30))
            return {"access_token": access_token, "token_type": "bearer"}
        except Exception as e:
            raise e