Diabetes Prediction App

A machine learning-powered web application built with Streamlit that predicts the likelihood of diabetes based on patient health metrics. This app uses a trained classification model and provides detailed input guidelines to help users understand each health parameter.

 Features
Interactive Web Interface – Clean, dark-themed UI with real-time input controls
ML-Powered Prediction – Uses a pre-trained model (diabetes_model.pkl) to classify diabetes risk
Detailed Input Guidelines – Sidebar explanations and hover tooltips for every input field
Dual-Column Layout – Organized form layout for easy data entry
Visual Feedback – Color-coded prediction results with follow-up advice

 Input Parameters
Table
Parameter	Description	Typical Range
Pregnancies	Number of times pregnant	0 – 17
Glucose Level	Plasma glucose 2 hours after OGTT (mg/dL)	70 – 200
Blood Pressure	Diastolic blood pressure (mm Hg)	24 – 122
Skin Thickness	Triceps skin fold thickness (mm)	7 – 99
Insulin Level	2-Hour serum insulin (μU/mL)	0 – 846
BMI	Body Mass Index	18.0 – 67.1
Diabetes Pedigree Function	Genetic diabetes risk score	0.078 – 2.42
Age	Age in years	21 – 81

Installation
Prerequisites
Python 3.8+
pip package manager
Setup
bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/diabetes-prediction-app.git
cd diabetes-prediction-app

# 2. Create a virtual environment (recommended)
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ensure the model file is present
# Place 'diabetes_model.pkl' in the project root directory

Dependencies
plain
streamlit>=1.28.0
numpy>=1.24.0
scikit-learn>=1.3.0
joblib>=1.3.0
Save the above to a requirements.txt file and run pip install -r requirements.txt

Usage
Run the App
bash
streamlit run app.py
The app will open in your default browser at http://localhost:8501.
How to Use
Enter your health metrics in the input fields
Hover over the (?) icon next to each field for quick guidance
Expand the sidebar (left arrow) for detailed explanations of each parameter
Click Predict to get your result
Review the prediction and follow-up advice

 Model Details
Algorithm: Random Forest, StandardScaler
Training Dataset: Pima Indians Diabetes Dataset
Accuracy: 84.4% accuracy, 91.7% precision, 61.1% recall, 73.3% F1, 0.968 ROC-AUC
Features: 8 health parameters
Target: Binary classification (0 = No Diabetes, 1 = Diabetes)
Note: This app is for educational/demo purposes only. Always consult a healthcare professional for medical diagnosis.
