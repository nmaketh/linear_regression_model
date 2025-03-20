# prediction.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Load the saved model and scaler
best_model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# Initialize the FastAPI app
app = FastAPI()

# Define the input schema using Pydantic
class PredictionInput(BaseModel):
    Gender: int
    Age: float
    Profession: int
    Academic_Pressure: float
    Work_Pressure: float
    CGPA: float
    Study_Satisfaction: float
    Job_Satisfaction: float
    Sleep_Duration: int
    Dietary_Habits: int
    Degree: int
    Suicidal_Thoughts: int
    Work_Study_Hours: float
    Financial_Stress: float
    Family_History: int

# Define the prediction endpoint
@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        # Convert input data into a DataFrame
        features = [
            input_data.Gender,
            input_data.Age,
            input_data.Profession,
            input_data.Academic_Pressure,
            input_data.Work_Pressure,
            input_data.CGPA,
            input_data.Study_Satisfaction,
            input_data.Job_Satisfaction,
            input_data.Sleep_Duration,
            input_data.Dietary_Habits,
            input_data.Degree,
            input_data.Suicidal_Thoughts,
            input_data.Work_Study_Hours,
            input_data.Financial_Stress,
            input_data.Family_History
        ]
        
        # Create a DataFrame for consistency with training data
        feature_names = [
            'Gender', 'Age', 'Profession', 'Academic Pressure', 'Work Pressure', 'CGPA',
            'Study Satisfaction', 'Job Satisfaction', 'Sleep Duration', 'Dietary Habits',
            'Degree', 'Have you ever had suicidal thoughts ?', 'Work/Study Hours',
            'Financial Stress', 'Family History of Mental Illness'
        ]
        input_df = pd.DataFrame([features], columns=feature_names)
        
        # Scale the input data
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = best_model.predict(input_scaled)[0]
        
        return {"prediction": int(prediction)}  # Return prediction as an integer
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the app locally (for testing purposes)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
