# import FastAPI
from fastapi import FastAPI
from contextlib import asynccontextmanager
# contextmanager: managing the whole lifecycle
from app.core.config.db_config import load_env_config 
from database.session import Base, engine
# from models import ConsultationForm, InquiryForm, Users
from router.root_router import root_router
from fastapi.exceptions import RequestValidationError
from app.core.globalexception.error_response import validation_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.globalexception.exceptions import not_found_exception_handler
from app.core.middleware.jwt_middleware import JWTMiddleware

app=FastAPI(title="FastAPI Emp CRUD")

# app.add_middleware(JWTMiddleware)

router = root_router()
app.include_router(router=router)
# mount the root router to the FastAPI app
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# db_details = load_env_config()
# print(db_details)

# app.add_exception_handler(StarletteHTTPException, not_found_exception_handler)


@app.on_event("startup")
# startup event, when the application starts
async def startup_event():
    print("Database tables created")
    # create the tables in the database
    Base.metadata.create_all(bind=engine)

# @asynccontextmanager
# # asynccontextmanager: managing the whole lifecycle
# async def lifespan(app: FastAPI):
#     # This function will be called when the application starts and stops
#     print("Application startup")
#     Base.metadata.create_all(bind=engine)

@app.get("/") 
# get method, / route
def read_root():
    return {"Hello": "World"}
