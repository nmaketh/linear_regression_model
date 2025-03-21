from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
from fastapi.middleware.cors import CORSMiddleware

# Load the trained model and scaler
model = load("best_model.pkl")  # Replace with your model file
scaler = load("scaler.pkl")  # Replace with your scaler file

# Define input schema using Pydantic
class PredictionInput(BaseModel):
    gender: int
    age: float
    profession: int
    academic_pressure: float
    work_pressure: float
    cgpa: float
    study_satisfaction: float
    job_satisfaction: float
    sleep_duration: int
    dietary_habits: int
    degree: int
    suicidal_thoughts: int
    work_study_hours: float
    financial_stress: float
    family_history: int

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Create prediction endpoint
@app.post("/predict")
def predict(input_data: PredictionInput):
    # Convert input data to a numpy array
    input_array = np.array([
        input_data.gender,
        input_data.age,
        input_data.profession,
        input_data.academic_pressure,
        input_data.work_pressure,
        input_data.cgpa,
        input_data.study_satisfaction,
        input_data.job_satisfaction,
        input_data.sleep_duration,
        input_data.dietary_habits,
        input_data.degree,
        input_data.suicidal_thoughts,
        input_data.work_study_hours,
        input_data.financial_stress,
        input_data.family_history,
    ]).reshape(1, -1)

    # Scale the input data
    input_scaled = scaler.transform(input_array)

    # Make prediction
    prediction = model.predict(input_scaled)[0]

    # Return the prediction
    return {"prediction": prediction}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
