from sqlalchemy import Column, Integer, String, ForeignKey, Text, ARRAY, Boolean, DateTime
from sqlalchemy.orm import relationship
from src.global_knowledge.db import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(String(255), primary_key=True)
    title = Column(String, index=True)
    questions = relationship("Question", back_populates="quiz")
    exam = relationship("Exam", back_populates="quiz")

class Question(Base):
    __tablename__ = "questions"

    id = Column(String(255), primary_key=True)
    quiz_id = Column(String(255), ForeignKey("quizzes.id"))
    text = Column(Text)
    answers = Column(ARRAY(String))
    correct_answer = Column(Integer)
    quiz = relationship("Quiz", back_populates="questions")
    exam_question = relationship("ExamQuestion", back_populates="questions")

class User(Base):
    __tablename__ = "users"
    
    id = Column(String(255), primary_key=True)
    user_id = Column(String(50), unique=True)
    hashed_password = Column(String)
    admin_status = Column(Boolean)
    exam = relationship("Exam", back_populates="user")

class Exam(Base):
    __tablename__ = "exams"

    id = Column(String(255), primary_key=True)
    user_id = Column(String(50), ForeignKey("users.user_id"))
    quiz_id = Column(String(255), ForeignKey("quizzes.id"))
    finish_date = Column(DateTime(timezone=True))
    submit = Column(Boolean)
    user = relationship("User", back_populates="exams")
    quiz = relationship("Quiz", back_populates="exams")

    exam_question = relationship("ExamQuestion", back_populates="owner")

class ExamQuestion(Base):
    __tablename__ = "exam_questions"

    id = Column(String(255), primary_key=True)
    exam_id = Column(String(255), ForeignKey("exams.id"))
    question_id = Column(String(255), ForeignKey("questions.id"))
    page = Column(Integer)
    orders = Column(Integer)
    answers = Column(ARRAY(String))
    correct_answer = Column(Integer)
    check_answer = Column(Integer)

    owner = relationship("Exam", back_populates="exam_questions")
    question = relationship("Question", back_populates="exam_questions")

