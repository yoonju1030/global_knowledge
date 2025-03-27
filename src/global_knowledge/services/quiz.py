from src.global_knowledge.schemas import QuizCreate, QuestionBase
from sqlalchemy.orm import Session

from src.global_knowledge.models import Quiz, Question
from uuid import UUID, uuid4
class QuizService:
    def __init__(self):
        pass

    def make_quiz(self, quiz: QuizCreate, db: Session):
        try:
            question_list = list()
            for q in quiz.questions:
                question = Question(id=str(uuid4()), text=q.text, answers=q.answers, correct_answer=q.correct_answer)
                question_list.append(question)
            db_quiz = Quiz(id=str(uuid4()), title=quiz.title, questions=question_list)
            db.add(db_quiz)
            db.commit()
            return db_quiz.id
        except Exception as e:
            raise e



