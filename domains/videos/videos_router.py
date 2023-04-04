from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from domains.videos import videos_crud, videos_schema

router = APIRouter(
    prefix='/api/video'
)

@router.get('/list', response_model=list[videos_schema.GetMainList])
def video_list(db:Session=Depends(get_db)):
    _video_list = videos_crud.get_video_list(db)
    return  _video_list
