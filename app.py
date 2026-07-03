import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("water_model.pkl")

# Page settings
st.set_page_config(page_title="Daily Water Intake Predictor", page_icon="💧")

# Title
st.title("💧 Daily Water Intake Predictor")
st.write("Enter your details below to predict your daily water intake.")

# Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)
weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=65.0)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=172.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=30.0)
exercise = st.number_input("Exercise Minutes", min_value=0.0, max_value=300.0, value=30.0)

# Prediction
if st.button("Predict Water Intake"):
    data = np.array([[age, weight, height, temperature, exercise]])
    prediction = model.predict(data)

    st.success(f"💧 Predicted Daily Water Intake: **{prediction[0]:.2f} Liters**")

    st.info("""
### Input Summary
- Age
- Weight
- Height
- Temperature
- Exercise Minutes
""")