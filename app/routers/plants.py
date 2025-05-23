
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Plant

router = APIRouter(prefix="/plants", tags=["plants"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_plants(db: Session = Depends(get_db)):
    return [{"id": p.id, "code": p.code, "mother_id": p.mother_id} for p in db.query(Plant).all()]
