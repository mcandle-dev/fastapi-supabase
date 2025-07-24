import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Supabase 설정
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL과 SUPABASE_KEY가 설정되지 않았습니다.")

# Supabase 클라이언트 생성
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)