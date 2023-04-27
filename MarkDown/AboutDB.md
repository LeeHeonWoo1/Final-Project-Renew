### Models(Mysql사용)
DB내의 모든 테이블의 형태를 정의한다.  
|테이블 명|설명|
|---|---|
|Dataset|youtube에서 크롤링 한 영상 데이터. 썸네일 주소, iframe태그에 쓰일 링크, 제목이 있다.|
|User|회원가입 시 저장되는 회원 정보 테이블|
|Replies|영상에 달리는 댓글들에 대한 테이블. 댓글이 달린 영상을 알아야 하기에 외래키로 Dataset테이블과 연결하였고, Dataset에서도 조회할 수 있게 역참조 설정을 해주었다.|
|Board|게시판에 게시될 게시글들의 정보를 모아놓은 테이블.|
|Answer|게시판에 달리는 댓글들에 대한 테이블. 마찬가지로 Board테이블과 외래키로 연결, 역참조 설정|  

이후 alembic으로 테이블 자동생성. `alembic revision --autogenerate`로 테이블 생성 혹은 변경하는 실행문들이 담긴 리비전 파일을 생성하고 `alembic upgrade head`로 테이블을 자동 생성한다.

- 느꼈던 것
  + 큰 데이터를 다루는 것도 아닌데 굳이 MySQL을 고집했다 싶다. 다음에는 Sqlite3로 빠른 개발 이후에 MySQL or Postgre로 전환하는 식으로의 개발도 생각해야 할 듯 하다.

#### Query  
SqlAlchemy를 사용해서 개발을 진행했기에 SQL 쿼리문을 사용하지 않고 python 코드처럼 생긴 쿼리문을 사용했다.  
`[모든 데이터 조회]`
```py
from database import SessionLocal
from models import *

db = SessionLocal()
db.query(Answer).all()
```  

`[특정 ID값 하나만 조회]`
```py
# 2 way exist
db.query(Answer).get(1)
db.query(Answer).filter(Answer.id==1).all()
```  

`[특정 컬럼에 특정 문자열을 포함하는 항목 조회]`
```py
db.query(Answer).filter(Answer.content.like('%FastAPI%')).all()
```

###  MySql연결 시 사용했던 URL형식
sqlalchemy.url = mysql+pymysql://root:password@hostname:portnumber/databasename?charset=utf8