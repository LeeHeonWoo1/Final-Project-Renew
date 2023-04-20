from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from domains.board.Answer.answer_crud import create_answer
from domains.board.Answer.answer_schema import CreateAnswer

router = APIRouter(
  prefix= '/api/answer'
)

@router.post('/create_answer', status_code = status.HTTP_204_NO_CONTENT)
def answer_create(_create_answer: CreateAnswer, db:Session = Depends(get_db)):
  create_answer(db=db, _create_answer = _create_answer)