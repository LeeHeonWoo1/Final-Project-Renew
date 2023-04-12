from pydantic import BaseModel, validator

class Article(BaseModel):
    content: str
    writer: str

    @validator('content', 'writer')
    def not_null(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 게시글은 저장되지 않습니다. 내용을 입력해주세요.')
        return v

    class Config:
        orm_mode = True