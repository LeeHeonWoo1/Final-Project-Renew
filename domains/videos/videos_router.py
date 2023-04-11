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

@router.get('/random_list', response_model=list[videos_schema.GetMainList])
def random_video_list(db:Session=Depends(get_db)):
    _random_video_list = videos_crud.get_random_video_list(db=db)
    return _random_video_list

@router.get('/detail/{video_id}', response_model=videos_schema.GetMainList)
def get_video(video_id: int, db:Session=Depends(get_db)):
    _video = videos_crud.get_video(db, video_id)
    return _video

@router.post('/search', response_model=list[videos_schema.GetMainList])
def keyword_video_list(keyword:videos_schema.Keyword, db:Session = Depends(get_db)):
    return videos_crud.get_keyword_video(db=db, keyword=keyword.keyword)