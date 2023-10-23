from pydantic import BaseModel

class Question(BaseModel):
    id: int
    question_id: int
    test_question: str
    text_answer: str
    date: str
