import streamlit as st
import joblib
import pandas as pd
import json

# Load model
model = joblib.load("rf_model.pkl")

# Load columns
with open("model_columns.json") as f:
    columns = json.load(f)

st.title("Insurance Risk Prediction Simulator")

st.write("Estimate healthcare costs and risk profile based on user inputs.")

# Inputs
age = st.slider("Age", 18, 80)
bmi = st.slider("BMI", 15.0, 40.0)
children = st.slider("Number of Children", 0, 5)
smoker = st.selectbox("Smoker", ["yes", "no"])
sex = st.selectbox("Sex", ["male", "female"])
region = st.selectbox("Region", ["northwest", "northeast", "southwest", "southeast"])

# Create input structure
input_dict = {col: 0 for col in columns}

input_dict["age"] = age
input_dict["bmi"] = bmi
input_dict["children"] = children
input_dict["smoker_yes"] = 1 if smoker == "yes" else 0
input_dict["sex_male"] = 1 if sex == "male" else 0

if f"region_{region}" in input_dict:
    input_dict[f"region_{region}"] = 1

input_df = pd.DataFrame([input_dict])

# Prediction
if st.button("Predict"):

    prediction = model.predict(input_df)[0]

    st.subheader("Estimated Annual Cost")
    st.write(f"${prediction:,.0f}")

    # Risk score (do seu projeto!)
    risk_score = ((smoker == "yes")*2 + (bmi > 30) + (age > 50))

    st.subheader("Risk Score")
    st.write(f"{risk_score} (0–4 scale)")

    # Risk level
    if risk_score >= 3:
        st.error("High Risk Profile")
    elif risk_score == 2:
        st.warning("Moderate Risk")
    else:
        st.success("Low Risk")

    # Insight humano (importante!)
    if smoker == "yes":
        st.info("Smoking is one of the strongest drivers of healthcare costs.")
