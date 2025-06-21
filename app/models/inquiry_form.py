from sqlalchemy import JSON, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base
from datetime import datetime

class InquiryForm(Base):
    __tablename__ = "inquiry_forms"

    id= Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    phone_number = Column(String, index=True, nullable=False)
    preferred_country = Column(String, index=True, nullable=False)
    preferred_level = Column(String, index=True, nullable=False)
    preferred_course = Column(String, index=True, nullable=False)
    intake= Column(String, index=True, nullable=False)
    scores = Column(String, nullable=True)
    additional_info=Column(String, nullable=True)
    heard_from = Column(String, index=True, nullable=False)