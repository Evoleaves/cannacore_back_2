
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, varieties, mothers, plants, lots
import os
import uvicorn

app = FastAPI(title="Cannacore API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(varieties.router)
app.include_router(mothers.router)
app.include_router(plants.router)
app.include_router(lots.router)

@app.get("/")
def root():
    return {"message": "Cannacore API demo funcionando correctamente"}
    from app.routers import predict
app.include_router(predict.router)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
