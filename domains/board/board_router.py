from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy.orm import Session
from domains.board import board_crud, board_schema

router = APIRouter(
    prefix = '/api/board'
)

@router.post("/create_article", status_code=status.HTTP_204_NO_CONTENT)
def create_new_article(_article:board_schema.CreateArticle ,db: Session = Depends(get_db)):
    board_crud.create_article(db=db, _article = _article)

@router.get("/article_list", response_model=board_schema.ArticleList)
def get_article_list(db:Session = Depends(get_db), section:str='', page:int=0, size:int=10):
    total, _article_list = board_crud.get_article_list(db=db, section=section, skip=page*size, limit=size)
    return {"total":total, "article_list":_article_list}

@router.get("/get_one_article/{article_id}", response_model=board_schema.Article)
def get_one_article(article_id:int = 0, db:Session = Depends(get_db)):
    article = board_crud.get_one_article(db=db, article_id=article_id)
    return article

@router.delete('/delete_article/{article_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_one_article(article_id:int = 0, db:Session = Depends(get_db)):
    board_crud.delete_article(db=db, article_id=article_id)