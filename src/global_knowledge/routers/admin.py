from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.admin import AdminService
from src.global_knowledge.schemas import PageInfo
from src.global_knowledge.models import User
from src.global_knowledge.auth import get_current_user


admin_router = APIRouter(prefix="/admin")

@admin_router.post(
    "/page",
    summary="페이지 당 문제 갯수 세팅", 
    description="페이지 당 보여지는 문제 개수 를 page 값으로 지정하여 요청"
)
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