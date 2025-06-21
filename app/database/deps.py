from typing import Generator
from sqlalchemy.orm import Session
from database.session import SessionLocal

def get_db() -> Generator[Session, None, None]:
    # Generator function to provide a database session for each request
    # None: send type
    # 2nd None: return type
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
