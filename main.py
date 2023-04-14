from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domains.videos import videos_router
from domains.User import user_router
from domains.reply import reply_router
from domains.board import board_router

app = FastAPI()

origins = ['http://127.0.0.1:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

app.include_router(videos_router.router)
app.include_router(user_router.router)
app.include_router(reply_router.router)
app.include_router(board_router.router)