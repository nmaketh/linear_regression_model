Depression Prediction App



Overview



This project is a Depression Prediction App that uses a machine learning model to predict the likelihood of depression based on user inputs. The app is built using Flutter for the frontend and a Python-based API for the backend. The machine learning model is trained on a dataset containing various features such as age, gender, academic pressure, work pressure, and more.

Features
User-Friendly Interface: A clean and intuitive UI for entering input data.

Machine Learning Model: A trained model that predicts depression likelihood based on user inputs.

API Integration: The Flutter app communicates with a Python-based API to fetch predictions.

Responsive Design: The app is designed to work seamlessly on both mobile and tablet devices.

Technologies Used
Frontend: Flutter (Dart)

Backend: Python (FastAPI or Flask)

Machine Learning: Scikit-learn, Pandas, NumPy, matplotlib

Deployment: Render (for API), GitHub (for code hosting)

Project Structure
Copy
depression-prediction-app/
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

bash
Copy
git clone https://github.com/your-username/depression-prediction-app.git
cd depression-prediction-app/api
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Run the API:

bash
Copy
uvicorn main:app --host 0.0.0.0 --port 8000
The API will be available at http://localhost:8000.

Deploy the API:

Deploy the API to a cloud platform like Render or Heroku.

2. Frontend (Flutter App)
Install Flutter:

Follow the official Flutter installation guide.

Run the App:

bash
Copy
cd depression-prediction-app/flutter_app
flutter pub get
flutter run
Update API URL:

Open lib/main.dart and replace the API URL with your deployed API endpoint:

dart
Copy
final url = Uri.parse('https://your-api-url/predict');
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
Copy
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

License

Acknowledgments
Dataset: Kaggle

Flutter: Flutter Documentation

FastAPI: FastAPI Documentation

Contact
For questions or feedback, feel free to reach out:

Email: n.riak@alustudent.com

GitHub: nmaketh
