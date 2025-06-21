# session based specifications to work on our operations
from builtins import int, list, setattr
from sqlalchemy.orm import Session
from app.models.inquiry_form import InquiryForm
from app.schemas.inquiry_form_schema import InquiryFormCreate, InquiryFormUpdate, InquiryFormResponse

class InquiryFormRepo:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_InquiryForms(self) -> list[InquiryForm]:
        InquiryForms = self.db.query(InquiryForm).all()
        return InquiryForms
    
    def get_InquiryForm_by_id(self, InquiryForm_id: int) -> InquiryForm:
        InquiryForm = self.db.query(InquiryForm).filter(InquiryForm.id == InquiryForm_id).first()
        return InquiryForm
    
    def create_InquiryForm(self, inquiryForm: InquiryFormCreate) -> InquiryForm:
        db_InquiryForm = InquiryForm(
            first_name=inquiryForm.first_name,
            last_name=inquiryForm.last_name,
            email=inquiryForm.email,
            phone_number=inquiryForm.phone_number,
            preferred_country=inquiryForm.preferred_country,
            preferred_level=inquiryForm.preferred_level,
            preferred_course=inquiryForm.preferred_course,
            intake=inquiryForm.intake,
            scores=inquiryForm.scores,
            additional_info=inquiryForm.additional_info,
            heard_from=inquiryForm.heard_from
        )
        self.db.add(db_InquiryForm)
        self.db.commit()
        self.db.refresh(db_InquiryForm)
        return db_InquiryForm
    
    def delete_InquiryForm(self, InquiryForm_id: int):
        InquiryForm = self.db.query(InquiryForm).filter(InquiryForm.id==InquiryForm_id).first()
        if InquiryForm:
            self.db.delete(InquiryForm)
            self.db.commit()
            return True
        return False
    
    def update_InquiryForm(self, InquiryForm_id:int, InquiryForm_update)->InquiryForm:
        InquiryForm=self.db.query(InquiryForm).filter(InquiryForm.id==InquiryForm_id).first()
        if not InquiryForm:
            return None
        for key, value in InquiryForm_update.dict().items():
            setattr(InquiryForm, key, value)
        self.db.commit()
        self.db.refresh(InquiryForm)
        return InquiryForm
    
    # def update_append(self, InquiryForm_id:int, permissions)->InquiryForm:
    #     InquiryForm = self.db.query(InquiryForm).filter(InquiryForm.id==InquiryForm_id).first()
    #     if not InquiryForm:
    #         return None
    #     for key, value in permissions.dict().items():
    #         InquiryForm.permissions[key] = value 
    #     self.db.commit()
    #     self.db.refresh(InquiryForm) 
    #     return InquiryForm