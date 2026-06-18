from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ai", "failure_model.pkl")

model = joblib.load(MODEL_PATH)

class PredictionRequest(BaseModel):
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    network_usage: float

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/predict")
def predict(data: PredictionRequest):

    features = [[
        data.cpu_usage,
        data.memory_usage,
        data.disk_usage,
        data.network_usage
    ]]

    prediction = model.predict(features)

    return {
        "failure": "likely" if prediction[0] == 1 else "unlikely"
    }