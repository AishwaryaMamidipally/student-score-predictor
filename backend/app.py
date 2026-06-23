from fastapi import FastAPI
from pydantic import BaseModel
from backend.predictor import predict_score

app = FastAPI()

class StudentInput(BaseModel):
    hours_studied: float
    attendance: float
    previous_score: float

@app.get("/")
def home():
    return {"message": "Student Score Predictor API"}

@app.post("/predict")
def predict(input_data: StudentInput):
    prediction = predict_score(input_data.model_dump())

    return {
        "prediction_score": round(prediction, 2)
    }