"""
Main router for all backend endpoints
"""
from fastapi import APIRouter
from . import author_routing, book_routing, comment_routing, rating_routing, review_routing, user_routing, work_routing


router = APIRouter()
router.include_router(author_routing.router, prefix='/authors', tags=['Authors'])
router.include_router(book_routing.router, prefix='/books', tags=['Books'])
router.include_router(comment_routing.router, prefix='/comments', tags=['Comments'])
router.include_router(rating_routing.router, prefix='/ratings', tags=['Ratings'])
router.include_router(review_routing.router, prefix='/reviews', tags=['Reviews'])
router.include_router(user_routing.router, prefix='/users', tags=['Users'])
router.include_router(work_routing.router, prefix='/works', tags=['Woeks'])
