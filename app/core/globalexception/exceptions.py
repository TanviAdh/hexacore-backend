from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_404_NOT_FOUND

def get_object_or_404(obj, name="Resource"):
    if not obj:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"{name} not found")
    return obj

# global exception handler for 404 errors
async def not_found_exception_handler(request: Request, exec: StarletteHTTPException):
    if exec.status_code == HTTP_404_NOT_FOUND:
        path_parts = request.url.path.strip("/").split("/")
        entity= path_parts[1] if path_parts else "Resource"
        entity_name= entity.replace("-"," ").replace("_"," ").capitalize()
        return JSONResponse(
            status_code=HTTP_404_NOT_FOUND,
            content={
                "status": False,
                "message": f"{entity_name} not found at {request.url.path}",
                "path": request.url.path
            }
        )