from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    id: str
    name: str
    grade: str
    phone: str
    kakao_use: bool
    member_card_no: Optional[str] = None
    credit_card_name: Optional[str] = None
    credit_card_no: Optional[str] = None


class User(UserCreate):
    """
    Supabase users 테이블 구조:
    
    create table users (
        id text primary key,
        name text,
        grade text,
        phone text,
        kakao_use boolean,
        member_card_no text unique,
        credit_card_name text,
        credit_card_no text unique
    );
    """
    pass
