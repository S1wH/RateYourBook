"""
Main router for all backend endpoints
"""
from fastapi import APIRouter
from . import rating_routing


router = APIRouter()
router.include_router(rating_routing.router, prefix="/ratings", tags=["Ratings"])
