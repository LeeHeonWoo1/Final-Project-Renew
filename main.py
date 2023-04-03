from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['http://127.0.0.1:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ['*'],
)

@app.get('/')
def ge():
    return {"message":"get first commit"}
