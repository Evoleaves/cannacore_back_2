from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, varieties, mothers, plants, lots, sensors, predict

app = FastAPI(title="Cannacore Demo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(varieties.router)
app.include_router(mothers.router)
app.include_router(plants.router)
app.include_router(lots.router)
app.include_router(sensors.router)
app.include_router(predict.router)

@app.get("/")
def root():
    return {"message": "Cannacore API demo funcionando correctamente"}
