from database import SessionLocal
from models import Dataset
from sqlalchemy.orm import Session

def get_video_list(db:Session):
    video_list = db.query(Dataset).all()
    return video_list