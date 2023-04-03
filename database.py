from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'mysql+pymysql://root:11112222@127.0.0.1:3306/dancey?charset=utf8'

engine = create_engine(DB_URL)

Base = declarative_base()
meta = Base.metadata

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
