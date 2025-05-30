from sqlalchemy.orm import Session
from src.global_knowledge.schemas import (
    ExamInfo,
    ExamCreateResponse,
    ExamCreateQuestion,
    ExamQuestionInfo
)
from src.global_knowledge.models import Exam, ExamQuestion, Question, Setting
from typing import List
from sqlalchemy import select
import datetime
from uuid import uuid4


class ExamService:
    def __init__(self, user_id):
        self.user_id = user_id

    def create_quiz_obj(self, exam_info: ExamInfo, db: Session):
        try:
            exam_uuid = str(uuid4())
            new_exam = Exam(
                id=exam_uuid,
                user_id=self.user_id,
                quiz_id=exam_info.quiz_id,
                finish_date=datetime.datetime.now(),
                submit=False,
            )
            db.add(new_exam)
            question_list = self.create_quiz_exam_questions(
                exam_uuid, exam_info.quiz_id, db
            )

            db.commit()
            exam_create_resp = self.get_questions(exam_uuid, db)

            return exam_create_resp
        except Exception as e:
            raise e

    def get_questions(self, exam_uuid: str, db: Session):
        try:
            query = (
                select(Question, ExamQuestion)
                .join(ExamQuestion, Question.id == ExamQuestion.question_id)
                .filter(ExamQuestion.exam_id == exam_uuid)
            )
            results = db.execute(query).all()
            exam_create_questions = list()
            if len(results) > 0:
                for r in results:
                    exam_create_question = ExamCreateQuestion(
                        text=r[0].text,
                        answers=r[1].answers,
                        correct_answer=r[1].correct_answer,
                        check_answer=r[1].check_answer,
                        pages=r[1].page,
                        orders=r[1].orders,
                    )
                    exam_create_questions.append(exam_create_question)
            return ExamCreateResponse(
                exam_id=exam_uuid, exam_create_questions=exam_create_questions
            )
        except Exception as e:
            raise e

    def create_quiz_exam_questions(self, exam_uuid: str, quiz_id: str, db: Session):
        try:
            results = db.scalars(
                select(Question).where(Question.quiz_id == quiz_id)
            ).all()

            page_result = db.scalars(
                select(Setting).where(Setting.category == "page").order_by(Setting.set_date.desc())
            ).one()
            setting_page = page_result.value

            exam_question_list = list()
            if len(results) > 0:
                for idx in range(len(results)):
                    page = idx // setting_page
                    order = idx % setting_page
                    new_exam_question = ExamQuestion(
                        id=str(uuid4()),
                        exam_id=exam_uuid,
                        question_id=results[idx].id,
                        page=page,
                        orders=order,
                        answers=results[idx].answers,
                        correct_answer=results[idx].correct_answer,
                        check_answer=-1,
                    )
                    exam_question_list.append(new_exam_question)
                db.add_all(exam_question_list)
            return exam_question_list
        except Exception as e:
            raise e

    def submit_exam(self, exam_id: str, db: Session):
        try:
            db.query(Exam).filter_by(id=exam_id).update({"submit": True})
            db.commit()
            results = db.scalars(
                select(ExamQuestion)
                .where(ExamQuestion.exam_id == exam_id)
            ).all()
            answers = list(map(lambda x:{"id":x.id,"orders": x.orders, "question_id": x.question_id, "check_answer": x.check_answer, "correct_answer": x.correct_answer}, results))
            return answers
        except Exception as e:
            raise e
        
    def check_answer(self, exam_question_info: ExamQuestionInfo, db: Session):
        try:
            db.query(ExamQuestion).filter_by(id=exam_question_info.exam_question_id).update({"check_answer": exam_question_info.answer})
            db.commit()
        except Exception as e:
            raise e
