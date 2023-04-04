from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from domains.User.user_schema import CreateUser
from domains.User import user_crud, user_schema
from domains.User.user_crud import pwd_context

from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from starlette.config import Config

config = Config('.env')

SECRET_KEY = config('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))
ALGORITHM = 'HS256'

router = APIRouter(
    prefix='/api/user'
)

@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def sign_up(_user_create:CreateUser, db:Session = Depends(get_db)):
    user = user_crud.get_existing_user(db=db, user_create=_user_create) 
    if user:
        raise HTTPException(detail='이미 존재하는 아이디, 이메일, 닉네임입니다.', status_code=status.HTTP_409_CONFLICT)
    
    user_crud.create_user(db=db, user_create=_user_create)

@router.post('/login', response_model=user_schema.Token)
def login_for_token_access(form_data:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    # OAuth2PasswordRequestForm으로부터 사용자가 입력하는 username와 password에 대한 정보를 얻어올 수 있다.
    user = user_crud.get_user(db, form_data.username)

    if not user or not pwd_context.verify(form_data.password, user.password):
        # 로그인에 실패하면 헤더에 필요한 정보를 담아 error를 발생시킨다.
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='아이디 및 비밀번호를 확인하세요', headers={"WWW-Authenticate": "Bearer"})
    
    data = {
        "sub":user.username,
        "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }

    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token":access_token,
        "token_type":"bearer",
        "username": user.username
    }
    
