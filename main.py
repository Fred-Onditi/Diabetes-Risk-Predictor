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

# ──────────────────────────────────────────────────────────────
# GUIDELINES SIDEBAR
# ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Input Guidelines")
    st.markdown("---")

    st.subheader(" Pregnancies")
    st.markdown("""
    **What it means:** Number of times the patient has been pregnant.  
    **Typical range:** 0 – 17  
    **Why it matters:** Pregnancy can cause hormonal changes that affect insulin sensitivity. Gestational diabetes history increases type 2 diabetes risk.
    """)
    st.markdown("---")

    st.subheader(" Glucose Level")
    st.markdown("""
    **What it means:** Plasma glucose concentration (mg/dL) measured 2 hours after an oral glucose tolerance test (OGTT).  
    **Typical range:** 70 – 200 mg/dL  
    **Why it matters:** Elevated glucose is the primary indicator of diabetes. Normal fasting glucose is <100 mg/dL; ≥126 mg/dL suggests diabetes.
    """)
    st.markdown("---")

    st.subheader("Blood Pressure")
    st.markdown("""
    **What it means:** Diastolic blood pressure (mm Hg).  
    **Typical range:** 24 – 122 mm Hg  
    **Why it matters:** High blood pressure often coexists with diabetes and increases cardiovascular complications.
    """)
    st.markdown("---")

    st.subheader(" Skin Thickness")
    st.markdown("""
    **What it means:** Triceps skin fold thickness (mm).  
    **Typical range:** 7 – 99 mm  
    **Why it matters:** Measures subcutaneous fat, which correlates with overall body fat and insulin resistance.
    """)
    st.markdown("---")

    st.subheader(" Insulin Level")
    st.markdown("""
    **What it means:** 2-Hour serum insulin (μU/mL).  
    **Typical range:** 0 – 846 μU/mL  
    **Why it matters:** High insulin levels may indicate insulin resistance, where the body compensates by producing more insulin.
    """)
    st.markdown("---")

    st.subheader(" BMI")
    st.markdown("""
    **What it means:** Body Mass Index = weight(kg) / height(m)².  
    **Typical range:** 18.0 – 67.1  
    **Why it matters:** Higher BMI is strongly linked to type 2 diabetes. Overweight (≥25) and obese (≥30) categories carry elevated risk.
    """)
    st.markdown("---")

    st.subheader("Diabetes Pedigree Function")
    st.markdown("""
    **What it means:** A score estimating genetic diabetes risk based on family history.  
    **Typical range:** 0.078 – 2.42  
    **Why it matters:** Higher values indicate stronger family history of diabetes, increasing hereditary risk.
    """)
    st.markdown("---")

    st.subheader("Age")
    st.markdown("""
    **What it means:** Patient's age in years.  
    **Typical range:** 21 – 81 years  
    **Why it matters:** Type 2 diabetes risk increases significantly with age, especially after 45.
    """)

# ──────────────────────────────────────────────────────────────
# INPUT UI WITH HELP TOOLTIPS
# ──────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input(
        "Pregnancies", 
        min_value=0, 
        step=1,
        help="Number of times pregnant. Typical range: 0–17. Pregnancy hormones can affect insulin sensitivity."
    )

    glucose = st.number_input(
        "Glucose Level", 
        min_value=0,
        help="Plasma glucose (mg/dL) 2 hours after OGTT. Normal <100; diabetes ≥126."
    )

    blood_pressure = st.number_input(
        "Blood Pressure", 
        min_value=0,
        help="Diastolic blood pressure (mm Hg). Often elevated alongside diabetes."
    )

    skin_thickness = st.number_input(
        "Skin Thickness", 
        min_value=0,
        help="Triceps skin fold thickness (mm). Measures body fat; higher = more insulin resistance risk."
    )

with col2:
    insulin = st.number_input(
        "Insulin Level", 
        min_value=0,
        help="2-Hour serum insulin (μU/mL). High levels may signal insulin resistance."
    )

    bmi = st.number_input(
        "BMI", 
        min_value=0.0, 
        format="%.1f",
        help="Body Mass Index = weight(kg) / height(m)². Overweight ≥25; Obese ≥30."
    )

    dpf = st.number_input(
        "Diabetes Pedigree Function", 
        min_value=0.0, 
        format="%.3f",
        help="Genetic diabetes risk score based on family history. Higher = stronger hereditary risk."
    )

    age = st.number_input(
        "Age", 
        min_value=0, 
        step=1,
        help="Age in years. Risk increases significantly after age 45."
    )

# ──────────────────────────────────────────────────────────────
# PREDICTION
# ──────────────────────────────────────────────────────────────
if st.button('Predict'):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error('The model predicts that you are likely to have diabetes.')
        st.info("**Consult a healthcare professional** for proper diagnosis and management.")
    else:
        st.success('The model predicts that you are unlikely to have diabetes.')
        st.info("Maintain a healthy lifestyle to keep your risk low.")