from pydantic import BaseModel
from domains.reply.reply_schema import Reply

class GetMainList(BaseModel):
    id: int
    singer: str
    src: str
    youtube_url: str
    replies: list[Reply] = []

    class Config:
        orm_mode = True

class Keyword(BaseModel):
    keyword: str = ''