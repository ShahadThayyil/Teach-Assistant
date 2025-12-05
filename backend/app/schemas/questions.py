from pydantic import BaseModel
from typing import Optional, Dict

class QuestionBase(BaseModel):
    exam_id: int
    mcq: Optional[Dict] = None
    one_mark: Optional[Dict] = None
    three_mark: Optional[Dict] = None

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int

    class Config:
        orm_mode = True
