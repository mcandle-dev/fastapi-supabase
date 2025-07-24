# FastAPI Supabase User Management

FastAPI와 Supabase를 사용한 사용자 관리 시스템입니다.

## 기능

- 사용자 정보 등록
- 사용자 정보 조회
- 사용자 정보 수정
- 사용자 정보 삭제
- 웹 폼을 통한 사용자 등록

## 기술 스택

- FastAPI
- Supabase
- Jinja2 Templates
- Python 3.7+

## 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/mcandle/fastapi-supabase.git
cd fastapi-supabase
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate  # Windows
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

4. 환경 변수 설정
- `.env` 파일을 생성하고 다음 내용을 추가:
```
SUPABASE_URL=your-supabase-project-url
SUPABASE_KEY=your-supabase-anon-key
```

5. Supabase 테이블 생성
```sql
create table users (
    id text primary key,
    name text,
    grade text,
    phone text,
    kakao_use boolean,
    member_card_no text unique,
    credit_card_name text,
    credit_card_no text unique,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
```

## 실행 방법

```bash
uvicorn main:app --reload
```

서버가 실행되면 다음 URL에서 접근 가능합니다:
- 웹 폼: http://localhost:8000
- API 문서: http://localhost:8000/docs

## API 엔드포인트

- `GET /users/`: 모든 사용자 조회
- `GET /users/{user_id}`: 특정 사용자 조회
- `POST /users/`: 새 사용자 생성
- `PUT /users/{user_id}`: 사용자 정보 수정
- `DELETE /users/{user_id}`: 사용자 삭제

## 라이센스

MIT License

## 작성자

mcandle
