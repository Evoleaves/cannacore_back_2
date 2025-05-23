
from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from PIL import Image
import numpy as np
import tensorflow as tf
import io
import os

router = APIRouter(prefix="/predict", tags=["predict"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Simulamos el modelo IA para demo
class MockModel:
    def predict(self, x):
        return [[0.23, 0.77]]  # dummy prediction probabilities

# Cargar modelo TensorFlow real si existe, si no usar mock
MODEL_PATH = "model.h5"
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    model = MockModel()

@router.post("/")
async def predict_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        image = image.resize((224, 224))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array)
        result = prediction[0] if isinstance(prediction, (list, np.ndarray)) else []

        return {
            "filename": file.filename,
            "prediction": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
