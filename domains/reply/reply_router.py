from fastapi import APIRouter, status, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from domains.reply import reply_schema, reply_crud
from domains.videos import videos_crud
from domains.User.user_crud import get_user

router = APIRouter(
    prefix= '/api/reply'
)

@router.post('/create/{video_id}', status_code=status.HTTP_204_NO_CONTENT)
def create_reply(video_id:int, reply_create:reply_schema.CreateReply, db:Session = Depends(get_db)):
    video = videos_crud.get_video(db=db, video_id=video_id)
    user = get_user(db=db, username=reply_create.username)
    if not video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Can't find video")
    reply_crud.create_reply(db=db, video=video, _create_reply=reply_create, _writer=user.username)

@router.post('/get_reply/{video_id}', response_model= list[reply_schema.Reply])
def get_reply(username:str, video_id:int, db:Session = Depends(get_db)):
    reply = reply_crud.get_reply(db=db, writer=username, video_id=video_id)
    if not reply:
        raise ValueError('등록된 댓글이 없습니다.')
    return reply
