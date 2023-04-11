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