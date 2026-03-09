import streamlit as st
import numpy as np
import joblib

@st.cache_resource
def load_model():
    return joblib.load('diabetes_model.pkl')

try:
    model = load_model()
except Exception as e:
    st.error(f"Could not load model: {e}")
    st.info("Check if 'diabetes_model.pkl' is in the C:\\Users\\Admin\\Diabetes folder.")
    st.stop()
    
st.title('Diabetes Prediction App')
st.write('Enter the following details to predict the likelihood of diabetes:')

# Input UI
col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose Level", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
     
with col2:
    insulin = st.number_input("Insulin Level", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    age = st.number_input("Age", min_value=0, step=1)

if st.button('Predict'):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error('The model predicts that you are likely to have diabetes.')
    else:
        st.success('The model predicts that you are unlikely to have diabetes.')