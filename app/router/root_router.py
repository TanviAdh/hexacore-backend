from fastapi import APIRouter
from router.inquiry_form_router import router as inquiry_form_router
from router.consultation_form_router import router as consultation_form_router
from router.auth_router import router as auth_router
from router.login_router import router as login_router

def root_router():
    api_router = APIRouter(prefix="/api")
    api_router.include_router(inquiry_form_router)
    api_router.include_router(consultation_form_router)
    api_router.include_router(auth_router)
    api_router.include_router(login_router)
    return api_router