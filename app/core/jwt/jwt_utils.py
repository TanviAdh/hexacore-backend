# creation of token
# usage of token (consumption)
# validation of token
# Token: should integrate the permissions in role
# jwt is used for authorization
# It is preferred as everything is encrypted
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt


# constants
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300

# Token creation

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        print(f"expires_delta: {expires_delta}")
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    else:
        ACCESS_TOKEN_EXPIRE_MINUTES = 300  # Default expiration time
        print(f"ACCESS_TOKEN_EXPIRE_MINUTES: {ACCESS_TOKEN_EXPIRE_MINUTES}")
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

# Verify token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError: 
        # malpractices and all other errors handled by jwterror
        return None
    except Exception as e:
        print (f"An error occured while verifying the token: {e}")
        return None
    


    