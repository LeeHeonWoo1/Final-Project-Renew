from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy.orm import Session
from domains.board import board_crud, board_schema

router = APIRouter(
    prefix = '/api/board'
)

@router.post("/create_article", status_code=status.HTTP_204_NO_CONTENT)
def create_new_article(_article:board_schema.Article ,db: Session = Depends(get_db)):
    board_crud.create_article(db=db, _article = _article)

@router.get("/article_list", response_model=list[board_schema.Article])
def get_article_list(db:Session = Depends(get_db)):
    article_list = board_crud.get_article_list(db=db)
    return article_list