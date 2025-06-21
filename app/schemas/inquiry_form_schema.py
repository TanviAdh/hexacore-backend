from builtins import float, int, str
from typing import Dict, Optional
from pydantic import BaseModel
from datetime import datetime

class InquiryFormBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    preferred_country: str
    preferred_level: str
    preferred_course: str
    intake: str
    scores: Optional[Dict[str, float]] = None
    additional_info: Optional[str] = None
    heard_from: str

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class InquiryFormCreate(InquiryFormBase):
    pass

class InquiryFormResponse(InquiryFormBase):
    id: int
    
    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class InquiryFormUpdate(InquiryFormBase):
    pass