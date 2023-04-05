from pydantic import EmailStr, BaseModel, validator
# 아이디 찾기, 비밀번호 변경, 비밀번호 찾기 전용 스키마

class UserInformation(BaseModel):
    username:str
    email:str
    password:str

    class Config:
        orm_mode = True

# 위의 정보 불러올 때 사용
class UserID(BaseModel):
    username: str

# ID찾을 때 사용
class UserEmail(BaseModel):
    email:str

    class Config:
        orm_mode = True

# 비밀번호 변경
class ChangePassword(BaseModel):
    username:str
    email:EmailStr
    password1:str
    password2:str

    @validator('password2')
    def same_as(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v
