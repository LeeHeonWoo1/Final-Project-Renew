from domains.board import board_schema
from sqlalchemy.orm import Session
from models import Board
from datetime import datetime

def create_article(db: Session, _article: board_schema.CreateArticle):
    db_article = Board(content = _article.content,
                       writer = _article.writer,
                       write_date=datetime.now(),
                       title=_article.title,
                       section=_article.section)
    db.add(db_article)
    db.commit()

def get_article_list(db:Session, section:str, skip:int = 0, limit: int = 10):
    if section == '게시판':
        _article_list = db.query(Board).order_by(Board.id.desc())
    else:
        _article_list = db.query(Board).filter(Board.section == section).order_by(Board.id.desc())

    total = _article_list.count()
    article_list = _article_list.offset(skip).limit(limit).all()
    return total, article_list

def get_one_article(db:Session, article_id:int):
    return db.query(Board).get(article_id)

def delete_article(db:Session, article_id: int):
    target_article = db.query(Board).get(article_id)
    db.delete(target_article)
    db.commit()
    
def modify_article(db:Session, article_id:int, new_article:board_schema.CreateArticle):
    article = db.query(Board).get(article_id)
    article.content = new_article.content
    article.write_date = new_article.write_date
    