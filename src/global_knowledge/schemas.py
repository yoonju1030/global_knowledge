from pydantic import BaseModel
from typing import List


class QuestionBase(BaseModel):
    text: str
    answers: List[str]
    correct_answer: int


class QuizCreate(BaseModel):
    title: str
    questions: List[QuestionBase]

    class Config:  # 외부 클래스의 동작을 구성하거나 커스터마이징하는 데 사용 주로 이름이 Config,Meta
        orm_mode = True  # pydatic v1
        from_attributes = True


class QuizResponse(BaseModel):
    msg: str


class QuestionSearchByQuiz(BaseModel):
    id: str


class UserInfo(BaseModel):
    user_id: str
    password: str


class ExamInfo(BaseModel):
    quiz_id: str


class ExamSubmitInfo(BaseModel):
    exam_id: str

class ExamQuestionInfo(BaseModel):
    exam_question_id: str
    answer: int


class ExamCreateQuestion(BaseModel):
    text: str
    answers: List[str]
    correct_answer: int
    check_answer: int
    pages: int
    orders: int


class ExamCreateResponse(BaseModel):
    exam_id: str
    exam_create_questions: List[ExamCreateQuestion]

class PageInfo(BaseModel):
    page: int