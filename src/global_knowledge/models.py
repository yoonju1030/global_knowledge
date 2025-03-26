from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db import Base

class Quiz(Base):
    __tablename__ = 'quizzes'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    questions = relationship("Question", back_populates="quiz")

class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    text = Column(Text)
    correct_answer = Column(String)
    quiz = relationship("Quiz", back_populates="questions")