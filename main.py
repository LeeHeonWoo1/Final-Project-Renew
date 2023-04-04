from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domains.videos import videos_router
from domains.User import user_router

app = FastAPI()

origins = ['http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

app.include_router(videos_router.router)
app.include_router(user_router.router)