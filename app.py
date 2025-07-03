import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.joblib")

st.title("🌾 Crop Prediction App")
st.write("Enter soil and climate details to predict the suitable crop.")

ph = st.number_input("Soil pH", 3.0, 10.0, 6.5)
ec = st.number_input("Electrical Conductivity (EC)", 0.0, 5.0, 1.0)
oc = st.number_input("Organic Carbon (OC)", 0.0, 10.0, 2.5)
potassium = st.number_input("Potassium (ppm)", 0.0, 200.0, 50.0)
nitrogen = st.number_input("Nitrogen (ppm)", 0.0, 200.0, 50.0)
phosphorous = st.number_input("Phosphorous (ppm)", 0.0, 200.0, 50.0)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)

if st.button("Predict Crop"):
    features = np.array([[ph, ec, oc, potassium, nitrogen, phosphorous, temperature]])
    prediction = model.predict(features)[0]
    st.success(f"✅ Suggested Crop: **{prediction.upper()}**")
