from sqlalchemy.orm import Session
from app.schemas.inquiry_form_schema import InquiryFormBase, InquiryFormCreate, InquiryFormUpdate, InquiryFormResponse
from app.repos.inquiry_form_repo import InquiryFormRepo
from fastapi import HTTPException

class InquiryFormService:
    def __init__(self, db: Session):
        self.db = db
        self.inquiry = InquiryFormRepo(db)

    def get_all_inquiry_forms(self):
        return self.inquiry.get_all_InquiryForms()

    def get_inquiryForm_by_id(self, inquiry_id: int):
        inquiry = self.inquiry.get_InquiryForm_by_id(inquiry_id)
        if not inquiry:
            raise HTTPException(status_code=404, detail="Form not found")
        return inquiry

    def create_inquiry_form(self, inquiry_form: InquiryFormCreate):
        return self.inquiry.create_InquiryForm(inquiry_form)

    def update_inquiry_forms(self, inquiry_form_id: int, inquiry_form_data: InquiryFormUpdate):
        updated_inquiry_form= self.inquiry.update_InquiryForm(inquiry_form_id, inquiry_form_data)
        if not updated_inquiry_form:
            raise HTTPException(status_code=404, detail="inquiry forms not found")
        return updated_inquiry_form
    
    def delete_inquiry_forms(self, inquiry_forms_id: int):
        deleted = self.inquiry.delete_InquiryForm(inquiry_forms_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="inquiry forms not found")
        return deleted
