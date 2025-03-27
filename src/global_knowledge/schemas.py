
from pydantic import BaseModel
from typing import List

class QuestionBase(BaseModel):
    text: str
    answers: List[str]
    correct_answer: int

class QuizCreate(BaseModel):
    title: str
    questions: List[QuestionBase]

    class Config: # 외부 클래스의 동작을 구성하거나 커스터마이징하는 데 사용 주로 이름이 Config,Meta
        orm_mode = True #pydatic v1
        from_attributes = True

class QuizResponse(BaseModel):
    msg: str

class QuestionSearchByQuiz(BaseModel):
    id: str

class SignUpInfo(BaseModel):
    user_id: str
    password: str
