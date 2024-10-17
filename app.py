from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np  # Import numpy
import pandas as pd

# Load the model once
model = joblib.load(r"C:\Users\Dell\Downloads\Scholarship_prediction-main\Scholarship_prediction-main\model.pkl")

# Define the Pydantic model for the request body
class Prediction(BaseModel):
    feature1: float
    feature2: float
    feature3: float  # Fix typo here

app = FastAPI()

@app.post("/predict")
def predict(request: Prediction):
    features = np.array([[request.feature1, request.feature2, request.feature3]])  # Create feature array
    prediction = model.predict(features)
    prediction = prediction[0]

    return {"prediction": prediction}
