from fastapi import APIRouter, Depends
from src.global_knowledge.schemas import QuizCreate, QuizResponse
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.quiz import QuizService
from src.global_knowledge.models import User
from src.global_knowledge.auth import get_current_user


quiz_router = APIRouter(prefix="/register")


@quiz_router.post(
    "/quizzes/", 
    response_model=QuizResponse, 
    summary="Quiz 생성 엔드포인트", 
    description="여러 문제를 포함하는 퀴즈를 생성한다. answers 리스트에는 보기를 넣고 보기중 정답의 인덱스를 correct_answer 값으로 한다"
)
def create_quiz(
    quiz: QuizCreate, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):
    try:
        if current_user.admin_status:
            quiz_service = QuizService()
            added_quiz_id = quiz_service.make_quiz(quiz, db)
            return QuizResponse(msg=added_quiz_id)
        else:
            raise Exception("권한이 없습니다")
    except Exception as e:
        raise e
    

