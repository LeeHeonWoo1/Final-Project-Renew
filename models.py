from sqlalchemy import Column, INT, VARCHAR, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Dataset(Base):
    __tablename__ = 'Dance_dataset'
    # __table_args__ = {'extend_existing': True}

    id = Column(INT, autoincrement=True, primary_key=True)
    singer = Column(VARCHAR(500), nullable=False)
    src = Column(VARCHAR(500), nullable=False)
    youtube_url = Column(VARCHAR(500), nullable=False)

class User(Base):
    __tablename__ = 'UserInformation'
    # __table_args__ = {'extend_existing': True}

    id = Column(INT, autoincrement=True, primary_key=True)
    username = Column(VARCHAR(50), nullable=False, unique=True)
    name = Column(VARCHAR(50), nullable=False, unique=True)
    nickname = Column(VARCHAR(50), nullable=False, unique=True)
    password = Column(VARCHAR(150), nullable=False)
    email = Column(VARCHAR(150), nullable=False, unique=True)

class Replies(Base):
    __tablename__ = "Replies"
    # __table_args__ = {'extend_existing':True}

    id = Column(INT, autoincrement=True, primary_key=True)
    content = Column(VARCHAR(500), nullable=False)
    writer = Column(VARCHAR(500), nullable=False)
    write_date = Column(DateTime, nullable=False)
    video_id = Column(INT, ForeignKey('Dance_dataset.id'))
    video = relationship("Dataset", backref="replies")

class Board(Base):
    __tablename__ = 'board'
    # __table_args__ = {'extend_existing':True}

    id = Column(INT, autoincrement=True, primary_key=True)
    title = Column(VARCHAR(500), nullable=False)
    section = Column(VARCHAR(50), nullable=False)
    content = Column(VARCHAR(500), nullable=False)
    writer = Column(VARCHAR(500), nullable=False)
    write_date = Column(DateTime, nullable=False)
    
class Answer(Base):
    __tablename__ = 'answer_for_board'
    # __table_args__ = {"extend_existing":True}
    
    id = Column(INT, autoincrement=True, primary_key=True)
    answer = Column(VARCHAR(500), nullable=False)
    answer_writer = Column(VARCHAR(60))
    write_date = Column(DateTime, nullable=False)
    article_id = Column(INT, ForeignKey('board.id'))
    article = relationship("Board", backref="answers")