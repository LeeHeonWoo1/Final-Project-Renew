### API  
domains에 모여있는 각 파일들이 API이며, 각 역할은 아래와 같다.  

|파일 이름|설명|
|---|---|
|~_schema.py|pydantic을 이용한 입-출력 값을 검증하는 파일|
|~_crud.py|말 그대로 CRUD(생성, 조회, 갱신, 삭제)를 담당하는 파일|
|~_router.py|router파일. crud파일의 함수를 포함하고 있으며, 실질적으로 api주소를 받아 데이터를 넘겨주는 파일이다.|  

### Dependency Injection(의존성 주입)
~_router.py파일을 살펴보면 항상 보이는 것이 있다.  
```py
def myfunc(db:Session = Depends(get_db)):
    pass
```  
db에 타입 어노테이션으로 Session유형임을 알려주고 FastAPI에서 제공하는 Depends로 get_db라는 함수를 파라미터로 제공한다. 의존성 주입이란 뭘까?  

우선 get_db함수를 먼저 살펴보면,
```py
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
```  
db 객체를 생성하고 오류에 관계없이 그를 닫는다. 이러한 함수 하나만으로도 코드의 가독성이 올라가는데, Depends함수를 통해 가독성을 한층 더 올려준다. 사실 아직까지 의존성 주입에 대한 개념은 감이 잘 잡히지 않는다. 추가적으로 더 정리가 필요할 듯 하다.

