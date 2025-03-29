from fastapi import APIRouter, Depends
from src.global_knowledge.schemas import ExamInfo, ExamCreateResponse, ExamSubmitInfo
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.exam import ExamService
from src.global_knowledge.models import User
from src.global_knowledge.auth import get_current_user

exam_router = APIRouter(prefix="/exam")


@exam_router.post("/quiz", response_model=ExamCreateResponse)
def exam_quiz(
    exam_info: ExamInfo,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        user_id = current_user.id
        exam_service = ExamService(user_id)
        exam_create_resp = exam_service.create_quiz_obj(exam_info, db)
        return exam_create_resp
    except Exception as e:
        raise e


@exam_router.post("/quiz/submit")
def submit_exam_quiz(
    exam_submit_info: ExamSubmitInfo,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        user_id =current_user.id
        exam_service = ExamService(user_id)
        results = exam_service.submit_exam(exam_submit_info.exam_id, db)
        return results

    except Exception as e:
        raise e


@exam_router.post("/quiz/question")
def submit_exam_quiz(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    try:
        # 문제 답 체크
        pass
    except Exception as e:
        raise e
