from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prediction(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
async def predict(request: Prediction):
    # Replace this with your actual prediction logic
    prediction_value = request.feature1 + request.feature2 + request.feature3  # Example logic
    return {"prediction": prediction_value}
