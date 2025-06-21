# declare the schema based specifications to work on our operations
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator

class LoginBase(BaseModel):
    email: EmailStr
    password: str
    @field_validator('password')
    def validate_password(cls, value):
        print (value, len(value))
            #password between 6 and 8 characters
        if len(value) <= 6:         
            raise ValueError('Password must be longer than 6 characters')
        return value

    class config:
        orm_mode = True # to tell pydantic to use the ORM model as the source of data
        # Enable ORM mode to work with SQLAlchemy models

class LoginCreate(LoginBase):
    pass
   

class LoginResponse(LoginBase):
    pass
    
    class config:
        orm_mode = True # to tell pydantic to use the ORM model as the source of data
        # Enable ORM mode to work with SQLAlchemy models

# class LoginTokenResponse(LoginResponse):
#     access_token: str
#     token_type: str
#     # token_type: bearer token
#     # access_token: encrypted alphanumeric value

    
