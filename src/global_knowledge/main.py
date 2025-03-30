import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.global_knowledge.routers.router import api_router

app = FastAPI(
    title="lyj_Quiz",  # API 제목
    description="""
        백엔드 개발자 지원자용 실무 과제에 해당하는 기능들입니다.

        login과 signup을 제외한 모든 기능은 authorization 이 필요합니다.
        1. 로그인 메서드를 통하여 access token을 발급받으시고
        2. 이외의 요청을 진행할 때마다 헤더에
        {"Authorization": "Bearer {발급받은 토큰}"} 을 추가하여 요청해주세요

        발급받은 token은 30분까지 지속됩니다.
    """,  # API 설명
    version="1.0.0" 
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
