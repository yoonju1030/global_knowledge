from fastapi import APIRouter
from src.global_knowledge.routers.quiz import quiz_router
from src.global_knowledge.routers.test import test_router

api_router = APIRouter()
api_router.include_router(quiz_router)
api_router.include_router(test_router)
