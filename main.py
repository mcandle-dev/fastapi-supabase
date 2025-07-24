from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models.user import User, UserCreate
from database import supabase
from typing import List

app = FastAPI()

# 정적 파일과 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 입력 폼 화면 표시
@app.get("/")
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# 폼 제출 처리
@app.post("/submit")
async def submit_form(
    request: Request,
    id: str = Form(...),
    name: str = Form(...),
    grade: str = Form(...),
    phone: str = Form(...),
    kakao_use: bool = Form(...),
    member_card_no: str = Form(...),
    credit_card_name: str = Form(...),
    credit_card_no: str = Form(...)
):
    try:
        user = UserCreate(
            id=id,
            name=name,
            grade=grade,
            phone=phone,
            kakao_use=kakao_use,
            member_card_no=member_card_no,
            credit_card_name=credit_card_name,
            credit_card_no=credit_card_no
        )
        response = supabase.table('users').insert(user.dict()).execute()
        return templates.TemplateResponse("success.html", {
            "request": request,
            "user": response.data[0]
        })
    except Exception as e:
        return templates.TemplateResponse("form.html", {
            "request": request,
            "error": str(e)
        })

# 기존 API 엔드포인트들...
@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    try:
        response = supabase.table('users').insert(user.dict()).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str):
    try:
        response = supabase.table('users').select("*").eq('id', user_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="User not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/", response_model=List[User])
async def list_users():
    try:
        response = supabase.table('users').select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user: UserCreate):
    try:
        response = supabase.table('users').update(user.dict()).eq('id', user_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="User not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    try:
        response = supabase.table('users').delete().eq('id', user_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

