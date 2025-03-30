from fastapi import APIRouter, Depends
from src.global_knowledge.schemas import ExamInfo, ExamCreateResponse, ExamSubmitInfo, ExamQuestionInfo
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.exam import ExamService
from src.global_knowledge.models import User
from src.global_knowledge.auth import get_current_user

exam_router = APIRouter(prefix="/exam")


@exam_router.post(
    "/quiz", 
    response_model=ExamCreateResponse,
    summary="시험 생성 엔드포인트", 
    description="시험 생성을 원하는 quiz의 id(uuid)를 quiz_id 값으로 지정해 요청한다"
)
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


@exam_router.post(
    "/quiz/submit",
    summary="시험 최종 제출 엔드포인트", 
    description="제출을 원하는 시험의 id(uuid) exam_id 값으로 지정해 요청한다."
)
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


@exam_router.post(
    "/quiz/question",
    summary="문제 답 체크 엔드포인트", 
    description="풀고자하는 문제의 id(uuid)를 exam_question_id 값으로, 답의 인덱스를 answer 값으로 지정해 요청한다."
)
def submit_exam_quiz(
    exam_question_info: ExamQuestionInfo,
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    try:
        user_id = current_user.id
        exam_service = ExamService(user_id)
        exam_service.check_answer(exam_question_info, db)
    except Exception as e:
        raise e
