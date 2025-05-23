
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import User

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return [{"id": u.id, "username": u.username} for u in db.query(User).all()]
