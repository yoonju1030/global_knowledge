from fastapi import APIRouter
from global_knowledge.routers.quiz import register_router
# from src.routers.transform import transform_router

api_router=APIRouter()
api_router.include_router(register_router)
# api_router.include_router(transform_router)
