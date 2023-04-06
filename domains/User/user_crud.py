from passlib.context import CryptContext
from sqlalchemy.orm import Session
from domains.User.user_schema import CreateUser
from domains.User.find_schema import UserInformation, ChangePassword
from models import User

# bcrypt알고리즘을 사용하는 CryptContext 객체 생성
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_user(db:Session, user_create: CreateUser):
    db_user = User(username = user_create.username,
                   name=user_create.name,
                   nickname = user_create.nickname,
                   # 객체를 이용해 암호 해시화
                   password = pwd_context.hash(user_create.password1),
                   email = user_create.email)
    db.add(db_user)
    db.commit()

def get_existing_user(db:Session, user_create:CreateUser):
    # DB에 이미 등록된 사용자가 있는지 조회
    return db.query(User).filter((User.username == user_create.username)|(User.email == user_create.email)|(User.nickname == user_create.nickname)).first()

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def change_password(db:Session, user:UserInformation, change_pwd:ChangePassword):
    user.password = pwd_context.hash(change_pwd.password1)
    db.add(user)
    db.commit()