from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from core.jwt.jwt_utils import verify_token

EXCLUDE_PATHS= ["/api/auth/login", "/api/employee/create", "/api/role/create"]

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # request: request that is raised by the client
        # call_next: call the next middleware or the endpoint (after the last middleware)
        # the way we will register the middleware, they will be executed in that same order
        # it will go from middleware to root router to specific router to service, to repo,to database
        # buffering area, middleware processing will be done here
        if request.url.path in EXCLUDE_PATHS:
            print ("Middleware in excluded paths")
            return await call_next(request)
        
        token = request.headers.get("X-AUTH-Token")
        if not token:
            return JSONResponse(status_code=401, content={"detail": "Missing token"})
            # inside the HTTPException, JSONResponse is used
        
        decoded = verify_token(token)
        if not decoded:
            return JSONResponse(status_code=401, content={"detail": "Invalid token"})
        response = await call_next(request)
        return response
    
        