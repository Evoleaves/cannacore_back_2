
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Variety

router = APIRouter(prefix="/varieties", tags=["varieties"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_varieties(db: Session = Depends(get_db)):
    varieties = db.query(Variety).all()
    return [v.name for v in varieties]
