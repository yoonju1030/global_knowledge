from sqlalchemy import Column, Integer, String, ForeignKey, Text, ARRAY
from sqlalchemy.orm import relationship
from src.global_knowledge.db import Base
from uuid import UUID, uuid4


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(String(255), primary_key=True)
    title = Column(String, index=True)
    questions = relationship("Question", back_populates="quiz")

class Question(Base):
    __tablename__ = "questions"

    id = Column(String(255), primary_key=True)
    quiz_id = Column(String(255), ForeignKey("quizzes.id"))
    text = Column(Text)
    answers = Column(ARRAY(String))
    correct_answer = Column(Integer)
    quiz = relationship("Quiz", back_populates="questions")
