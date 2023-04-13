from pydantic import BaseModel, validator
from datetime import datetime

class Article(BaseModel):
    id:int
    title: str
    content: str
    writer: str
    section: str
    write_date: datetime

    class Config:
        orm_mode = True

class CreateArticle(BaseModel):
    title: str
    content: str
    writer: str
    section: str

    @validator('title', 'section', 'content', 'writer')
    def not_null(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 게시글은 저장되지 않습니다. 내용을 입력해주세요.')
        return v

    class Config:
        orm_mode = True

class ArticleList(BaseModel):
    total: int = 0
    article_list: list[Article] = []