from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')  # Save scaler from Task 1

class WineInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: int
    total_sulfur_dioxide: int
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.post('/predict')
def predict(input_data: WineInput):
    try:
        data = np.array([[input_data.fixed_acidity, input_data.volatile_acidity, 
                        input_data.citric_acid, input_data.residual_sugar,
                        input_data.chlorides, input_data.free_sulfur_dioxide,
                        input_data.total_sulfur_dioxide, input_data.density,
                        input_data.pH, input_data.sulphates, input_data.alcohol]])
        data_scaled = scaler.transform(data)
        prediction = model.predict(data_scaled)
        return {"prediction": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
