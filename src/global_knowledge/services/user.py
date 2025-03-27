from sqlalchemy.orm import Session
from src.global_knowledge.models import User
from src.global_knowledge.schemas import SignUpInfo
from fastapi import HTTPException
from src.global_knowledge.auth import hash_password
from uuid import UUID, uuid4

class UserService:
    def __init__(self):
        pass

    def signup(self, signup_info: SignUpInfo ,db: Session):
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