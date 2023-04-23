from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from domains.board.board_crud import get_one_article
from domains.board.Answer.answer_crud import create_answer
from domains.board.Answer.answer_schema import CreateAnswer

router = APIRouter(
  prefix= '/api/answer'
)

@router.post('/create_answer/{article_id}', status_code = status.HTTP_204_NO_CONTENT)
def answer_create(_create_answer: CreateAnswer, article_id:int ,db:Session = Depends(get_db)):
  article = get_one_article(db=db, article_id=article_id)
  if not article:
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="존재하지 않는 게시글에는 실행할 수 없는 작업입니다.")
    
  create_answer(db=db, article=article, _create_answer = _create_answer, article_id=article_id)