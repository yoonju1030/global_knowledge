from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.test import TestService
from src.global_knowledge.schemas import QuizResponse, QuestionSearchByQuiz
from src.global_knowledge.models import User
from src.global_knowledge.auth import get_current_user


test_router = APIRouter(prefix="/test")

@test_router.get(
    "/select/",
    summary="전체 퀴즈 조회 엔드포인트"
)
def select_all_quiz_list(
    current_user: User = Depends(get_current_user),   
    db: Session = Depends(get_db)
):
    try:
        if current_user.admin_status:
            test_service = TestService()
            quiz_list = test_service.select_all_quiz_list(db)
            return quiz_list
        else:
            raise Exception("권한이 없습니다")
    except Exception as e:
        raise e
    
@test_router.post(
    '/select/questions',
    summary="퀴즈 별 문제 조회 엔드포인트", 
    description="조회를 원하는 퀴즈의 id(uuid) id 값으로 지정해 요청한다."
)
def select_questions_by_quiz(
    quiz_id: QuestionSearchByQuiz, 
    current_user: User = Depends(get_current_user),   
    db: Session = Depends(get_db)
):
    try:
        if current_user.admin_status:
            test_service = TestService()
            quiz_list = test_service.select_questions_by_quiz(quiz_id.id, db)
            return quiz_list
    except Exception as e:
        raise e