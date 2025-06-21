from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.schemas.inquiry_form_schema import InquiryFormCreate, InquiryFormUpdate, InquiryFormResponse
from app.services.inquiry_form_service import InquiryFormService
from app.repos.inquiry_form_repo import InquiryFormRepo

router = APIRouter(prefix="/inquiry", tags=["inquiry"])

@router.post("/create", response_model=InquiryFormResponse)
def create_inquiry_form(form: InquiryFormCreate, db: Session = Depends(get_db)):
    service = InquiryFormService(db)
    return service.create_inquiry_form(form)

# post method usage with create endpoint
@router.get("/", response_model=list[InquiryFormResponse])
def get_inquiry_forms(db: Session = Depends(get_db)):
    service = InquiryFormService(db)
    forms = service.get_all_inquiry_forms()
    if len(forms) > 0:
        return forms
    else:
        raise HTTPException(status_code=404, detail="No inquiry forms found")

@router.put("/update/{id}", response_model=InquiryFormResponse)
def update_inquiry_form(id: int, updates: InquiryFormUpdate, db: Session = Depends(get_db)):
    service = InquiryFormService(db)
    updated_form = service.update_inquiry_forms(id, updates)
    return updated_form

@router.delete("/delete/{id}")
def delete_inquiry_form(id:int, db: Session=Depends(get_db)):
    service= InquiryFormService(db)
    deleted = service.delete_inquiry_forms(id)
    if not deleted:
         raise HTTPException(status_code=404, detail="inquiry form not found")
    return {"message": f"inquiry form {id} deleted successfully"}
# @router.put("/append/{id}", response_model=RoleResponse)
# def update_append(id:int, permissions:PermissionsUpdate, db:Session=Depends(get_db)):
#     service=RoleService(db)
#     appended_role=service.update_append(id,permissions)
#     return appended_role
