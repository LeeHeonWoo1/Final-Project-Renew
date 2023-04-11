from pydantic import BaseModel, validator

class Article(BaseModel):
    id: int
    content: str
    writer: str
    write_date: str

    @validator('content')
    def not_null(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 게시글은 저장되지 않습니다. 내용을 입력해주세요.')
        return v
