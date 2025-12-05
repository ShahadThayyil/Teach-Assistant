from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.models import Question
from app.schemas.questions import QuestionCreate, QuestionResponse

router = APIRouter(prefix="/api/v1/questions", tags=["questions"])

# Create a new question
@router.post("/", response_model=QuestionResponse)
def create_question(payload: QuestionCreate, db: Session = Depends(get_db)):
    new_question = Question(
        exam_id=payload.exam_id,
        mcq=payload.mcq,
        one_mark=payload.one_mark,
        three_mark=payload.three_mark
    )
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

# Get all questions for an exam
@router.get("/exam/{exam_id}", response_model=List[QuestionResponse])
def get_questions_for_exam(exam_id: int, db: Session = Depends(get_db)):
    questions = db.query(Question).filter(Question.exam_id == exam_id).all()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found for this exam")
    return questions

# Get a single question by ID
@router.get("/{question_id}", response_model=QuestionResponse)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question
