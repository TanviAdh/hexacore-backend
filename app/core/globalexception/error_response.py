from fastapi import Request 
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException

# function of each inmport 
# Request: to get the request object
# JSONResponse: to return a JSON response
# RequestValidationError: to handle validation errors
# HTTP_422_UNPROCESSABLE_ENTITY: to set the status code for validation errors
# HTTPException: to handle HTTP exceptions

def format_validation_error(exec: RequestValidationError):
    # formatted={}
    # for err in exec.errors():
    #     field = ".".join(str(loc) for loc in err['loc'] if loc!='body')
    #     formatted[field] = err['msg']
    # return formatted
    error_map= {}
    for err in exec.errors():
        loc = err.get("loc",[])
        if "body" in loc:
            field = loc[1]
            if err['msg'].lower() == "field required":
                error_map[field]=f"{field.replace('_',' ').capitalize()} is required"
            else:
                error_map[field]= err['msg']
    return error_map
# FIELD_ERROR_MESSAGES = {

#     "first_name": "First name is missing",

#     "last_name": "Last name is missing",

#     "email": "Email address is missing",

#     "phone": "Phone number is missing"

# }

# def format_validation_errors(exc: RequestValidationError):

#     error_map = {}

#     for err in exc.errors():

#         loc = err.get("loc", [])

#         if "body" in loc:

#             field = loc[-1]

#             msg = err["msg"]

#             if msg.lower() == "field required":

#                 error_map[field] = FIELD_ERROR_MESSAGES.get(field, f"{field} is missing")

#             else:

#                 error_map[field] = msg  # <- Custom message from @field_validator

#     return error_map

def validation_exception_handler(request:Request, exec: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status": False,
            "message": "Validation Error",
            "errors": format_validation_error(exec)
        }
    )