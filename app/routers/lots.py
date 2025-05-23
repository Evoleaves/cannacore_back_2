
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Lot

router = APIRouter(prefix="/lots", tags=["lots"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_lots(db: Session = Depends(get_db)):
    return [{
        "id": l.id,
        "code": l.code,
        "variety_id": l.variety_id,
        "mother_id": l.mother_id,
        "start_date": str(l.start_date),
        "end_date": str(l.end_date),
        "plant_count": l.plant_count
    } for l in db.query(Lot).all()]
