from sqlalchemy.orm import Session
from domains.board.Answer.answer_schema import CreateAnswer
from models import Answer, Board
from datetime import datetime

def create_answer(db:Session, article:Board, article_id: Board.id, _create_answer: CreateAnswer):
  new_answer = Answer(answer = _create_answer.content, 
                      article = article,
                      article_id = article_id, 
                      answer_writer=_create_answer.writer, 
                      write_date=datetime.now())
  db.add(new_answer)
  db.commit()