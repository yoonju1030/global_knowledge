from sqlalchemy import select
from src.global_knowledge.models import Quiz, Question


class TestService:
    def __init__(self):
        pass

    def select_all_quiz_list(self, db):
        try:
            query = select(Quiz).select_from(Quiz)
            res = db.execute(query).scalars().all()
            return list(map(lambda x: {"id": x.id, "title": x.title}, res))
        except Exception as e:
            raise e

    def select_questions_by_quiz(self, quiz_id, db):
        try:
            results = db.scalars(
                select(Question).where(Question.quiz_id == quiz_id)
            ).all()
            if len(results) > 0:
                return results
            else:
                return []
        except Exception as e:
            raise e
