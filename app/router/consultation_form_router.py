from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.deps import get_db
from schemas.consultation_form_schema import ConsultationFormCreate, ConsultationFormUpdate, ConsultationFormResponse
from services.consultation_form_service import ConsultationFormService
from repos.consultation_form_repo import ConsultationFormRepo

router = APIRouter(prefix="/consultation", tags=["Consultation"])

@router.post("/create", response_model=ConsultationFormResponse)
def create_consultation_form(form: ConsultationFormCreate, db: Session = Depends(get_db)):
    service = ConsultationFormService(db)
    return service.create_consultation_form(form)

# post method usage with create endpoint
@router.get("/", response_model=list[ConsultationFormResponse])
def get_consultation_forms(db: Session = Depends(get_db)):
    service = ConsultationFormService(db)
    forms = service.get_all_consultation_forms()
    if len(forms) > 0:
        return forms
    else:
        raise HTTPException(status_code=404, detail="No consultation forms found")

@router.put("/update/{id}", response_model=ConsultationFormResponse)
def update_consultation_form(id: int, updates: ConsultationFormUpdate, db: Session = Depends(get_db)):
    service = ConsultationFormService(db)
    updated_form = service.update_consultation_forms(id, updates)
    return updated_form

@router.delete("/delete/{id}")
def delete_consultation_form(id:int, db: Session=Depends(get_db)):
    service= ConsultationFormService(db)
    deleted = service.delete_consultation_forms(id)
    if not deleted:
         raise HTTPException(status_code=404, detail="Consultation form not found")
    return {"message": f"Consultation form {id} deleted successfully"}
# @router.put("/append/{id}", response_model=RoleResponse)
# def update_append(id:int, permissions:PermissionsUpdate, db:Session=Depends(get_db)):
#     service=RoleService(db)
#     appended_role=service.update_append(id,permissions)
#     return appended_role
