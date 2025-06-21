from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.jwt.jwt_utils import create_access_token
from app.database.deps import get_db
from app.schemas.auth_schema import LoginRequest
from app.schemas.login_schema import LoginCreate, LoginResponse
from app.services.login_service import LoginService
from app.repos.login_repo import UsersRepo

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

@router.post("/create", response_model=LoginResponse)
def create_consultation_form(form: LoginCreate, db: Session = Depends(get_db)):
    service = LoginService(db)
    return service.create_user(email=form.email, password=form.password)


