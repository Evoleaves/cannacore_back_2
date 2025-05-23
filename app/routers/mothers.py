
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Mother

router = APIRouter(prefix="/mothers", tags=["mothers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_mothers(db: Session = Depends(get_db)):
    return [{"id": m.id, "code": m.code, "variety_id": m.variety_id} for m in db.query(Mother).all()]
