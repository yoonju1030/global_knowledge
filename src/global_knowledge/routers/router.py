from fastapi import APIRouter
from src.global_knowledge.routers.quiz import quiz_router

# from src.routers.transform import transform_router

api_router = APIRouter()
api_router.include_router(quiz_router)
# api_router.include_router(transform_router)
