from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.admin import AdminService
from src.global_knowledge.schemas import PageInfo
from src.global_knowledge.models import User
from src.global_knowledge.auth import get_current_user


admin_router = APIRouter(prefix="/admin")

@admin_router.post("/page")
def set_page(
    page_info: PageInfo,
    current_user: User = Depends(get_current_user),        
    db: Session = Depends(get_db)
):
    try:
        if current_user.admin_status:
            admin_service = AdminService()
            res = admin_service.set_page(page_info.page, db)
            return res
        else:
            raise Exception("권한이 없습니다")
    except Exception as e:
        raise e