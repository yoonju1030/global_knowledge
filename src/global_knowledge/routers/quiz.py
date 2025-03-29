from fastapi import APIRouter, HTTPException, Request, Depends
from typing import Union
from src.global_knowledge.schemas import QuizCreate, QuizResponse
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.quiz import QuizService


quiz_router = APIRouter(prefix="/register")


@quiz_router.post("/quizzes/", response_model=QuizResponse)
def create_quiz(quiz: QuizCreate, db: Session = Depends(get_db)):
    try:
        quiz_service = QuizService()
        added_quiz_id = quiz_service.make_quiz(quiz, db)
        return QuizResponse(msg=added_quiz_id)
    except Exception as e:
        raise e
    
@quiz_router.post("/quizzes/delete", response_model=QuizResponse)
def delete_quiz(quiz: QuizCreate, db: Session = Depends(get_db)):
    try:
        quiz_service = QuizService()
        added_quiz_id = quiz_service.make_quiz(quiz, db)
        return QuizResponse(msg=added_quiz_id)
    except Exception as e:
        raise e
