from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.test import TestService
from src.global_knowledge.schemas import QuizResponse, QuestionSearchByQuiz


test_router = APIRouter(prefix="/test")

@test_router.get("/select/")
def select_all_quiz_list(db: Session = Depends(get_db)):
    try:
        test_service = TestService()
        quiz_list = test_service.select_all_quiz_list(db)
        return quiz_list
    except Exception as e:
        raise e
    
@test_router.post('/select/questions')
def select_questions_by_quiz(quiz_id: QuestionSearchByQuiz, db: Session = Depends(get_db)):
    try:
        test_service = TestService()
        quiz_list = test_service.select_questions_by_quiz(quiz_id.id, db)
        return quiz_list
    except Exception as e:
        raise e