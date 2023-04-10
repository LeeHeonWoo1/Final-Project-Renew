from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from domains.User import user_crud, user_schema, find_schema
from domains.User.user_crud import pwd_context
from SendMail import gmail_sender
from random import randint

from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from starlette.config import Config

config = Config('.env')

SECRET_KEY = config('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))
ALGORITHM = 'HS256'

MAIL_SENDER = config('MAIL_SENDER')
SENDER_PASSWORD=config('SENDER_PASSWORD')

router = APIRouter(
    prefix='/api/user'
)

@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def sign_up(_user_create:user_schema.CreateUser, db:Session = Depends(get_db)):
    user = user_crud.get_existing_user(db=db, user_create=_user_create) 
    if user:
        raise HTTPException(detail='이미 존재하는 아이디, 이메일, 닉네임입니다.', status_code=status.HTTP_409_CONFLICT)
    
    user_crud.create_user(db=db, user_create=_user_create)

@router.post('/login', response_model=user_schema.Token)
def login_for_token_access(form_data:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = user_crud.get_user(db, form_data.username)

    if not user or not pwd_context.verify(form_data.password, user.password):
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

@router.post('/user-inform', response_model=find_schema.UserInformation)
def get_user_id(_user:find_schema.UserID, db:Session = Depends(get_db)):
    user = user_crud.get_user(db=db, username=_user.username)
    return user

# 아이디 찾을 때 사용
@router.post('/user-email', status_code=status.HTTP_204_NO_CONTENT)
def get_user_email(_user:find_schema.FindID, db:Session = Depends(get_db)):
    user_info = user_crud.get_user_email(db=db, email=_user.email)

    if user_info.email == _user.email and user_info.name == _user.name:
        mail_sender = gmail_sender(MAIL_SENDER, _user.email, SENDER_PASSWORD)
        mail_sender.msg_set("[Dancey] 아이디 확인 메일이 도착했습니다.", f"아이디는 {user_info.username}입니다.")
        mail_sender.smtp_connect_send()
        mail_sender.smtp_disconnect()

# 비밀번호 변경 전 인증절차
@router.post('/validation', status_code=status.HTTP_201_CREATED)
def email_validation(_user:find_schema.FindPassword, db:Session = Depends(get_db)):
    val_number = randint(9999, 99999)

    user = user_crud.get_user(db=db, username=_user.username)
    if not user:
        raise HTTPException(detail='이름, 이메일 주소를 확인하세요.', status_code=status.HTTP_409_CONFLICT)

    if user.username == _user.username and user.email == _user.email:
        mail_sender = gmail_sender(MAIL_SENDER, _user.email, SENDER_PASSWORD)
        mail_sender.msg_set("[Dancey] 인증메일이 도착했습니다.", f"인증번호는 : {val_number}입니다. 입력창에 입력해주세요")
        mail_sender.smtp_connect_send()
        mail_sender.smtp_disconnect()
    
    return val_number

# 비밀번호 변경
@router.put('/change-password', status_code=status.HTTP_204_NO_CONTENT)
def change_password(change_inform:find_schema.ChangePassword, db:Session=Depends(get_db)):
    _user = user_crud.get_user(db=db, username=change_inform.username)
    if not _user:
        raise HTTPException(detail='존재하지 않는 사용자입니다. ', status_code=status.HTTP_409_CONFLICT)
    
    if (_user.username != change_inform.username) or (_user.email != change_inform.email):
        raise HTTPException(detail='잘못된 아이디 혹은 이메일입니다.', status_code=status.HTTP_409_CONFLICT)
    
    user_crud.change_password(db = db, user = _user, change_pwd = change_inform)

@router.delete('/sign_out', status_code=status.HTTP_204_NO_CONTENT)
def sign_out(_sign_out:user_schema.SignOut, db:Session = Depends(get_db)):
    sign_out_user = user_crud.get_user(username = _sign_out.username, db = db)
    if not sign_out_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="이미 탈퇴 처리된 사용자이거나, 존재하지 않는 사용자 입니다.")
    
    if (sign_out_user.username != _sign_out.username) or (not pwd_context.verify(_sign_out.password, sign_out_user.password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="아이디 혹은 비밀번호를 확인하세요.")
    
    user_crud.delete_user(db=db, delete_user=sign_out_user)

