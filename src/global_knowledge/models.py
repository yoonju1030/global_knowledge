from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.global_knowledge.db import Base
from uuid import UUID, uuid4


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(String(30), primary_key=True, default=str(uuid4()))
    title = Column(String, index=True)
    questions = relationship("Question", back_populates="quiz")


#### Quiz ####
# id


class Question(Base):
    __tablename__ = "questions"

    id = Column(String(30), primary_key=True, default=str(uuid4()))
    quiz_id = Column(String(30), ForeignKey("quizzes.id"))
    text = Column(Text)
    correct_answer = Column(String)
    quiz = relationship("Quiz", back_populates="questions")
