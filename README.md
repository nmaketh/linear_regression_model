Depression Prediction App



Overview



This project is a Depression Prediction App that uses a machine learning model to predict the likelihood of depression based on user inputs. The app is built using Flutter for the frontend and a Python-based API for the backend. The machine learning model is trained on a dataset containing various features such as age, gender, academic pressure, work pressure, and more.



Features



User-Friendly Interface: A clean and intuitive UI for entering input data.

Machine Learning Model: A trained model that predicts depression likelihood based on user inputs.

API Integration: The Flutter app communicates with a Python-based API to fetch predictions.

Responsive Design: The app is designed to work seamlessly on both mobile and tablet devices.

SEE MY DEMO VIDEO HERE: https://youtu.be/2g3Y0lT2TjI



Technologies Used



Frontend: Flutter (Dart)

Backend: Python (FastAPI or Flask)

Machine Learning: Scikit-learn, Pandas, NumPy, matplotlib

Deployment: Render (for API), GitHub (for code hosting)



Dataset



Description



The dataset contains information about students and their mental health, including features such as age, gender, academic pressure, work pressure, CGPA, and more. The target variable is `Depression`, which represents the likelihood of depression.

Source



The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/hopesb/student-depression-dataset)



Machine Learning Models
Models Implemented


1. Linear Regression (SGDRegressor)
2. Decision Tree Regressor
3. Random Forest Regressor
   

Evaluation Metrics




| Model                      | Training MSE     | Testing MSE     |
|----------------------------|------------------|-----------------|
| Linear Regression (SGD)    | 0.12             | 0.12            |
| Decision Tree Regressor    | 0.12             | 0.13            |
| Random Forest Regressor    | 0.07             | 0.11            |




Best Model


The Random Forest Regressor was selected as the best model due to its lowest testing MSE.



API

Endpoints



1. **GET `/`**: Welcome message.
   ```json
   {
     "message": "Welcome to the Depression Prediction API!"
   }

   

Project Structure


linear_regression/summative/
├── api/                        # Backend API code
│   ├── main.py                 # API entry point
│   ├── model.pkl               # Trained machine learning model
│   ├── requirements.txt        # Python dependencies
├── flutter_app/                # Flutter app code
│   ├── lib/
│   │   ├── main.dart           # Flutter app entry point
│   │   ├── prediction_page.dart# UI for prediction form
│   ├── pubspec.yaml            # Flutter dependencies
├── README.md                   # Project documentation


Swagger UI



The API documentation is available at https://prediction-api-ife7.onrender.com/docs.


Mobile App



Features


Prediction Page: A form to input data and view predictions.


Input Fields: Text boxes for all features (e.g., age, gender, academic pressure, etc.).


Predict Button: Triggers the API call to fetch predictions.


Output Display: Displays the predicted depression score.







How It Works



User Input:

The user enters data into the Flutter app (e.g., age, gender, academic pressure, etc.).

API Request:

The app sends the input data to the Python-based API via a POST request.

Prediction:

The API processes the input data using the trained machine learning model and returns a prediction.

Display Result:

The app displays the prediction to the user.

Setup Instructions
1. Backend (API)
Clone the Repository:


git clone https://github.com/nmaketh/linear_regression.git
cd linear_regression/summative/API


Install Dependencies:


pip install -r requirements.

Run the API:

uvicorn main:app --host 0.0.0.0 --port 8000

The API will be available at http://localhost:8000.

Deploy the API:

Deploy the API to a cloud platform like Render or Heroku.

2. Frontend (Flutter App)
Install Flutter:

Follow the official Flutter installation guide.

Run the App:


cd linear_regression/summative/flutter_app


flutter pub get


flutter run

Update API URL: https://prediction-api-ife7.onrender.com

Open lib/main.dart and replace the API URL with your deployed API endpoint:


final url = Uri.parse('https://prediction-api-ife7.onrender.com');

Machine Learning Model
Dataset
The model is trained on a dataset containing the following features:

Gender

Age

Profession

Academic Pressure

Work Pressure

CGPA

Study Satisfaction

Job Satisfaction

Sleep Duration

Dietary Habits

Degree

Suicidal Thoughts

Work/Study Hours

Financial Stress

Family History

Training

Preprocessing:

Handle missing values, encode categorical variables, and normalize numerical features.

Model Selection:

Use algorithms like Logistic Regression, Random Forest, or Gradient Boosting.

Evaluation:

Evaluate the model using metrics like accuracy, precision, recall, and F1-score.

Saving the Model

Save the trained model using joblib or pickle:

python

import joblib
joblib.dump(model, 'model.pkl')
API Endpoints
POST /predict
Description: Predicts the likelihood of depression based on input data.

Request Body:

json
Copy
{
  "gender": 1,
  "age": 25,
  "profession": 2,
  "academic_pressure": 3.5,
  "work_pressure": 4.0,
  "cgpa": 3.2,
  "study_satisfaction": 2.5,
  "job_satisfaction": 3.0,
  "sleep_duration": 1,
  "dietary_habits": 2,
  "degree": 3,
  "suicidal_thoughts": 0,
  "work_study_hours": 8.5,
  "financial_stress": 2.0,
  "family_history": 1
}
Response:

json
Copy
{
  "prediction": 0.47
}




Screenshots
Input Form	Prediction Result
Input Form	Prediction Result



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
