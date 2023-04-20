from pydantic import BaseModel, validator
from datetime import datetime

class Answer(BaseModel):
  id: int
  content: str
  writer: str
  write_date: datetime

  class Config:
    orm_mode = True
    
class CreateAnswer(BaseModel):
  writer: str
  content: str
  
  @validator('content')
  def not_null(cls, v):
    if not v or not v.strip():
      raise ValueError('빈 댓글은 저장되지 않습니다.')
    
    return v
  
  class Config:
    orm_mode = True
  