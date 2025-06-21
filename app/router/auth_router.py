from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.jwt.jwt_utils import create_access_token
from database.deps import get_db
from schemas.auth_schema import LoginRequest
from services.login_service import LoginService

router = APIRouter(prefix="/auth", tags=["Users"])

@router.post("/login")
def login_user(auth: LoginRequest, db: Session = Depends(get_db)):
    service = LoginService(db)
    emp = service.authenticate_user(email=auth.email, password=auth.password)
    if emp==None:
        raise HTTPException(status_code=404, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": auth.email})
    res = {"email":auth.email, "access_token": access_token, "token_type": "bearer"}
    return res
