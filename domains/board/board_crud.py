from domains.board import board_schema
from sqlalchemy.orm import Session
from models import Board
from datetime import datetime

def create_article(db: Session, _article: board_schema.Article):
    db_article = Board(content = _article.content, writer = _article.writer, write_date=datetime.now())
    db.add(db_article)
    db.commit()