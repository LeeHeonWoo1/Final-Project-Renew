from sqlalchemy import Column, INT, VARCHAR
from database import Base

class Dataset(Base):
    __tablename__ = 'Dance_dataset'
    __table_args__ = {'extend_existing': True}

    id = Column(INT, autoincrement=True, primary_key=True)
    singer = Column(VARCHAR(500), nullable=False)
    src = Column(VARCHAR(500), nullable=False)
    youtube_url = Column(VARCHAR(500), nullable=False)

class TestDataset(Base):
    __tablename__ = 'Test_dataset'
    __table_args__ = {'extend_existing': True}

    id = Column(INT, autoincrement=True, primary_key=True)
    singer = Column(VARCHAR(500), nullable=False)
    src = Column(VARCHAR(500), nullable=False)
    youtube_url = Column(VARCHAR(600), nullable=False)

class User(Base):
    __tablename__ = 'UserInformation'
    __table_args__ = {'extend_existing': True}

    id = Column(INT, autoincrement=True, primary_key=True)
    username = Column(VARCHAR(50), nullable=False, unique=True)
    nickname = Column(VARCHAR(50), nullable=False, unique=True)
    password = Column(VARCHAR(150), nullable=False)
    email = Column(VARCHAR(150), nullable=False, unique=True)