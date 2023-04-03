from pydantic import BaseModel

class GetMainList(BaseModel):
    id: int
    singer: str
    src: str
    youtube_url: str

    class Config:
        orm_mode = True