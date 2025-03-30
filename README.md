## 실행

### poetry dependency 설치
```
poety install
```

### .env 생성
```
DB_ID=
DB_PW=
DB_HOST=
DB_NAME=
```

### backup.sql 세팅
- 해당 파일에는 기본 user, 관리자 admin 한명 씩 추가되어 있습니다.
- 일반 유저 - id: test , pw: 1234
- 관리자 유저 - id: admin, pw: 1234
- 기본 퀴즈 1개 , 문제 3개 추가되어 있으며 시험 한개를 수행하고 제출까지 완료한 상태입니다.

### 실행 cmd
```
poetry run uvicorn src.global_knowledge.main:app --reload
```

## docs
```
http://{실행 서버 ip or 127.0.0.1}:8000/docs
```
위 url에 swagger 문서로 확인해주시기 바랍니다.

- 실행 중 이슈 발생 시 meoliet1030@gmail.com 으로 연락 부탁드립니다.