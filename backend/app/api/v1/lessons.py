from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.models import LessonPlan
from app.schemas.lessonplan import LessonPlanCreate, LessonPlanResponse

router = APIRouter(prefix="/api/v1/lessonplan", tags=["lessonplan"])

@router.get("/{lessonplan_id}", response_model=LessonPlanResponse)
def get_lessonplan(lessonplan_id: int, db: Session = Depends(get_db)):
    lessonplan = db.query(LessonPlan).filter(LessonPlan.id == lessonplan_id).first()
    if not lessonplan:
        raise HTTPException(status_code=404, detail="Lesson plan not found")
    return lessonplan

@router.post("/generate", response_model=LessonPlanResponse)
def create_lessonplan(payload: LessonPlanCreate, db: Session = Depends(get_db)):
    new_plan = LessonPlan(
        teacher_id=payload.teacher_id,
        topic=payload.topic,
        duration_hours=payload.duration_hours,
        plan=payload.plan
    )
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return new_plan
