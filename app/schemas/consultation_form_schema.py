from typing import Dict, Optional
from pydantic import BaseModel
from datetime import datetime

class ConsultationFormBase(BaseModel):
    full_name: str
    email: str
    phone_number: str
    academic_qualifications: Optional[str] = None
    subject_of_interest: Dict[str, bool]
    study_destination: Dict[str, bool]
    intake: Optional[str] = None
    standardized_test: Dict[str, bool]
    goals: Optional[str] = None
    heard_from: str


    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class ConsultationFormCreate(ConsultationFormBase):
    pass

class ConsultationFormResponse(ConsultationFormBase):
    id: int
    
    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class ConsultationFormUpdate(ConsultationFormBase):
    pass