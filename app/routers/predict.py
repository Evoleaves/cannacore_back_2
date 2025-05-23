from fastapi import APIRouter

router = APIRouter(prefix="/predict", tags=["predict"])

@router.get("/")
def get_predict():
    return {{"message": "Simulación de /predict"}}
