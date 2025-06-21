# session based specifications to work on our operations
from builtins import int, list, setattr
from sqlalchemy.orm import Session
from models.consultation_form import ConsultationForm
from schemas.consultation_form_schema import ConsultationFormCreate, ConsultationFormUpdate, ConsultationFormResponse

class ConsultationFormRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_all_consultation_forms(self) -> list[ConsultationForm]:
        consultations = self.db.query(ConsultationForm).all()
        return consultations

    def get_consultation_by_id(self, consultationForm_id: int) -> ConsultationForm:
        consultation = self.db.query(ConsultationForm).filter(ConsultationForm.id == consultationForm_id).first()
        return consultation

    def create_ConsultationForm(self, consultationForm: ConsultationFormCreate) -> ConsultationForm:
        db_ConsultationForm = ConsultationForm(
            full_name=consultationForm.full_name,
            email=consultationForm.email,
            phone_number=consultationForm.phone_number,
            academic_qualifications=consultationForm.academic_qualifications,
            subject_of_interest=consultationForm.subject_of_interest,
            study_destination=consultationForm.study_destination,
            intake=consultationForm.intake,
            standardized_test=consultationForm.standardized_test,
            goals=consultationForm.goals,
            heard_from=consultationForm.heard_from
        )
        self.db.add(db_ConsultationForm)
        self.db.commit()
        self.db.refresh(db_ConsultationForm)
        return db_ConsultationForm
    
    def delete_ConsultationForm(self, ConsultationForm_id: int):
        ConsultationForm = self.db.query(ConsultationForm).filter(ConsultationForm.id==ConsultationForm_id).first()
        if ConsultationForm:
            self.db.delete(ConsultationForm)
            self.db.commit()
            return True
        return False
    
    def update_ConsultationForm(self, ConsultationForm_id:int, ConsultationForm_update)->ConsultationForm:
        ConsultationForm=self.db.query(ConsultationForm).filter(ConsultationForm.id==ConsultationForm_id).first()
        if not ConsultationForm:
            return None
        for key, value in ConsultationForm_update.dict().items():
            setattr(ConsultationForm, key, value)
        self.db.commit()
        self.db.refresh(ConsultationForm)
        return ConsultationForm
    
    # def update_append(self, ConsultationForm_id:int, permissions)->ConsultationForm:
    #     ConsultationForm = self.db.query(ConsultationForm).filter(ConsultationForm.id==ConsultationForm_id).first()
    #     if not ConsultationForm:
    #         return None
    #     for key, value in permissions.dict().items():
    #         ConsultationForm.permissions[key] = value 
    #     self.db.commit()
    #     self.db.refresh(ConsultationForm) 
    #     return ConsultationForm