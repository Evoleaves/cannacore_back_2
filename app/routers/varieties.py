from fastapi import APIRouter

router = APIRouter(prefix="/varieties", tags=["varieties"])

@router.get("/")
def get_varieties():
    return {{"message": "Simulación de /varieties"}}
