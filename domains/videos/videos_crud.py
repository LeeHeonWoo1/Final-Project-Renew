from models import Dataset
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

def get_video_list(db:Session):
    video_list = db.query(Dataset).all()
    return video_list

def get_random_video_list(db:Session):
    rand_vid_list = db.query(Dataset).order_by(func.rand()).limit(10).all()
    return rand_vid_list

def get_video(db: Session, video_id: int):
    return db.query(Dataset).get(video_id)

def get_keyword_video(db:Session, keyword: str):
    videos = db.query(Dataset).filter(Dataset.singer.ilike("%%{}%%".format(keyword))).all()
    return videos