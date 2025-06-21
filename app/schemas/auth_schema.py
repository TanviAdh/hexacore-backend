from builtins import ValueError
from pydantic import BaseModel, EmailStr, field_validator

class LoginRequest(BaseModel):
    email: EmailStr # type: ignore
    password: str

    @field_validator('password')
    def validate_password(cls, value):
        print (value, len(value))
        #password between 6 and 8 characters
        if len(value) <= 6:         
            raise ValueError('Password must be more than 6 characters long')
        return value