from pydantic import BaseModel, validator
from datetime import datetime

class CreateReply(BaseModel):
    content:str

    @validator('content')
    def not_null(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 댓글은 저장되지 않습니다. 댓글을 입력해주세요 !')
    
        return v
    
class Reply(BaseModel):
    id: int
    content:str
    write_date: datetime

    class Config:
        orm_mode = True
