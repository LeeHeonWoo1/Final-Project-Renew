from domains.reply.reply_schema import CreateReply
from datetime import datetime
from sqlalchemy.orm import Session
from models import Dataset, Replies

def create_reply(db: Session, video: Dataset, _create_reply: CreateReply):
    db_reply = Replies(content=_create_reply.content, write_date=datetime.now(), video=video)
    db.add(db_reply)
    db.commit()