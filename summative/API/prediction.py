
# Depression Prediction App

##Overview
This project is a Depression Prediction App that uses a machine learning model to predict the likelihood of depression based on user inputs. The app is built using Flutter for the frontend and a Python-based API for the backend. The machine learning model is trained on a dataset containing various features such as age, gender, academic pressure, work pressure, and more.


## Features
- User-Friendly Interface: A clean and intuitive UI for entering input data.
- Machine Learning Model: A trained model that predicts depression likelihood based on user inputs.
- API Integration: The Flutter app communicates with a Python-based API to fetch predictions.
- Responsive Design: The app is designed to work seamlessly on both mobile and tablet devices.

---

## Technologies Used
- Frontend: Flutter (Dart)
- Backend: Python (FastAPI)
- Machine Learning: Scikit-learn, Pandas, matplotlib, NumPy
- Deployment: Render (for API), GitHub (for code hosting)

---

##Dataset
###Description
The dataset contains information about students and their mental health, including features such as age, gender, academic pressure, work pressure, CGPA, and more. The target variable is `Depression`, which represents the likelihood of depression.

###Source
The dataset is sourced from [Kaggle]https://www.kaggle.com/datasets/hopesb/student-depression-dataset.

### Visualizations
1. Correlation Heatmap:
   ![Correlation Heatmap](screenshots/correlation_heatmap.png)
2. Distribution of Depression Scores:
   ![Depression Distribution](screenshots/depression_distribution.png)


## Machine Learning Models
### Models Implemented
1. Linear Regression (SGDRegressor)
2. Decision Tree Regressor
3. Random Forest Regressor

### Evaluation Metrics
| Model               | Training MSE | Testing MSE |
|----------------------------|------------------|-----------------|
| Linear Regression (SGD)    | 0.12             | 0.12            |
| Decision Tree Regressor    | 0.12             | 0.13            |
| Random Forest Regressor    | 0.07             | 0.11            |

### Best Model
The Random Forest Regressor was selected as the best model due to its lowest testing MSE.

## API
### Endpoints
1. GET `/`: Welcome message.
   ```json
   {
     "message": "Welcome to the Depression Prediction API!"
   }
POST /predict: Predicts the likelihood of depression based on input data.

Request Body:

json

{
  "gender": 1,
  "age": 25.0,
  "profession": 2,
  "academic_pressure": 3.0,
  "work_pressure": 4.0,
  "cgpa": 8.97,
  "study_satisfaction": 2.0,
  "job_satisfaction": 0.0,
  "sleep_duration": 0,
  "dietary_habits": 0,
  "degree": 4,
  "suicidal_thoughts": 1,
  "work_study_hours": 3.0,
  "financial_stress": 1.0,
  "family_history": 0
}
Response:

json
{
  "prediction": 0.47
}
Swagger UI
The API documentation is available at https://prediction-api-ife7.onrender.com.

Mobile App
Features
Prediction Page: A form to input data and view predictions.

Input Fields: Text boxes for all features (e.g., age, gender, academic pressure, etc.).

Predict Button: Triggers the API call to fetch predictions.

Output Display: Displays the predicted depression score.

Screenshots
Input Form	Prediction Result
Input Form	Prediction Result
How to Run the Project
1. Backend (API)
Clone the repository:

git clone https://github.com/nmaketh/linear_regression.git
cd linear_regression/summative/api
Install dependencies:


pip install -r requirements.txt
Run the API:


uvicorn prediction:app --host 0.0.0.0 --port 8000
2. Frontend (Flutter App)
Install Flutter:

Follow the official Flutter installation guide.

Run the app:
                        
cd depression-prediction-app/flutter_app
flutter pub get
flutter run
Video Demo
Watch the video demo here (replace with your actual link).

Contributing
Contributions are welcome! Follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a pull request.


Acknowledgments
Dataset: Kaggle

Flutter: Flutter Documentation

FastAPI: FastAPI Documentation

Contact
For questions or feedback, feel free to reach out:

Email: n.riak@alustudent.com

GitHub: nmaketh

