from fastapi import APIRouter, HTTPException, Request, Depends
from typing import Union
from src.global_knowledge.schemas import QuizCreate, QuizResponse
from sqlalchemy.orm import Session
from src.global_knowledge.models import Quiz, Question
from src.global_knowledge.db import get_db

quiz_router = APIRouter(prefix="/register")


@quiz_router.post("/quizzes/", response_model=QuizResponse)
def create_quiz(quiz: QuizCreate, db: Session = Depends(get_db)):
    db_quiz = Quiz(**quiz.dict())
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz
