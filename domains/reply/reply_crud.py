from domains.reply.reply_schema import CreateReply
from datetime import datetime
from sqlalchemy.orm import Session
from models import Dataset, Replies

def create_reply(db: Session, video: Dataset, _create_reply: CreateReply, _writer: str):
    db_reply = Replies(content=_create_reply.content, writer=_writer ,write_date=datetime.now(), video=video)
    db.add(db_reply)
    db.commit()

def get_reply(db:Session, writer:str, video_id:int):
    return db.query(Replies).filter((Replies.writer == writer)&(Replies.video_id == video_id)).all()