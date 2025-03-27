from fastapi import APIRouter
from src.global_knowledge.routers.quiz import quiz_router
from src.global_knowledge.routers.test import test_router
from src.global_knowledge.routers.user import user_router
from src.global_knowledge.routers.exam import exam_router

api_router = APIRouter()
api_router.include_router(quiz_router)
api_router.include_router(test_router)
api_router.include_router(user_router)
api_router.include_router(exam_router)
