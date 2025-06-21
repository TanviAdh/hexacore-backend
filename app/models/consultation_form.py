from sqlalchemy import JSON, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.session import Base
from datetime import datetime

class ConsultationForm(Base):
    __tablename__ = "consultation_forms"

    id= Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    phone_number = Column(String, index=True, nullable=False)
    academic_qualifications = Column(String, nullable=True)
    subject_of_interest = Column(JSON, nullable=True)
    study_destination = Column(JSON, nullable=True)
    intake = Column(String, nullable=True)
    standardized_test = Column(JSON, nullable=True)
    goals= Column(String, nullable=True)
    heard_from = Column(String, index=True, nullable=False)