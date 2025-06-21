from sqlalchemy.orm import Session
from app.schemas.consultation_form_schema import ConsultationFormCreate, ConsultationFormUpdate, ConsultationFormResponse
from app.repos.consultation_form_repo import ConsultationFormRepo
from fastapi import HTTPException

class ConsultationFormService:
    def __init__(self, db: Session):
        self.db = db
        self.consultation_form_repo = ConsultationFormRepo(db)

    def get_all_consultation_forms(self):
        return self.consultation_form_repo.get_all_consultation_forms()

    def get_consultation_by_id(self, consultation_id: int):
        consultation = self.consultation_form_repo.get_consultation_by_id(consultation_id)
        if not consultation:
            raise HTTPException(status_code=404, detail="Form not found")
        return consultation

    def create_consultation_form(self, consultation_form: ConsultationFormCreate):
        return self.consultation_form_repo.create_ConsultationForm(consultation_form)

    def update_consultation_forms(self, consultation_form_id: int, consultation_form_data: ConsultationFormUpdate):
        updated_consultation_form= self.consultation_form_repo.update_ConsultationForm(consultation_form_id, consultation_form_data)
        if not updated_consultation_form:
            raise HTTPException(status_code=404, detail="consultation forms not found")
        return updated_consultation_form
    
    def delete_consultation_forms(self, consultation_forms_id: int):
        deleted = self.consultation_form_repo.delete_ConsultationForm(consultation_forms_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="consultation forms not found")
        return deleted
