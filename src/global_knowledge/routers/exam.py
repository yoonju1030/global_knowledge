from fastapi import APIRouter, HTTPException, Request, Depends
from typing import Union
from src.global_knowledge.schemas import QuizCreate, QuizResponse
from sqlalchemy.orm import Session
from src.global_knowledge.db import get_db
from src.global_knowledge.services.exam import ExamService
from src.global_knowledge.models import User
from src.global_knowledge.auth import get_current_user

exam_router = APIRouter(prefix="/exam")

@exam_router.post("/quiz")
def exam_quiz(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        # 퀴즈 풀이 생성
        exam_service = ExamService()
    except Exception as e:
        raise e
    
@exam_router.post("/quiz/submit")
def submit_exam_quiz(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        # 퀴즈 풀이에 submit
        # 채점
        pass
    except Exception as e:
        raise e
    
@exam_router.post("/quiz/question")
def submit_exam_quiz(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        # 문제 답 체크
        pass
    except Exception as e:
        raise e