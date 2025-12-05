from pydantic import BaseModel
from typing import Dict

class LessonPlanCreate(BaseModel):
    teacher_id: int
    topic: str
    duration_hours: int
    plan: Dict

class LessonPlanResponse(LessonPlanCreate):
    id: int

    class Config:
        orm_mode = True
