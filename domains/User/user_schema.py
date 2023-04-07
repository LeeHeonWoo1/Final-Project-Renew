from pydantic import EmailStr, BaseModel, validator

class CreateUser(BaseModel):
    username: str
    name: str
    nickname: str
    password1: str
    password2: str
    email: EmailStr

    # 모든 입력란에 대해 빈값 허용 x
    @validator('username', 'name', 'nickname', 'password1', 'password2', 'email')
    def not_null(cls, v):
        if not v or not v.strip():
            raise ValueError('빈값은 허용하지 않습니다. 입력란을 확인하세요.')
        
        return v
    
    # 1차 비밀번호와 2차 비밀번호간의 검증
    @validator('password2')
    def same_as(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v
    
class SignOut(BaseModel):
    username: str
    email: str
    password: str

    @validator('username', 'email', 'password')
    def not_null(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용하지 않습니다.')
        return v
    
class Token(BaseModel):
    access_token: str
    token_type: str
    username: str