from fastapi import HTTPException
from sqlalchemy.orm import Session
from repos.login_repo import UsersRepo

class LoginService:
    def __init__(self, db:Session):
        self.db=db
        self.users_repo= UsersRepo(db)

    def create_user(self, email, password):
        return self.users_repo.create_user(email=email, password=password)
    
    def authenticate_user(self, email:str, password:str):
        user = self.users_repo.authenticate_user(email=email, password=password)
        if not user:
            return None
        return user
    def get_user_by_email(self, email: str):
        user= self.users_repo.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    
        
