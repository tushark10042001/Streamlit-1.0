import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("🏠 Dumb House Price Predictor")

size = st.number_input(
    "Enter house size (sq ft)",
    min_value=100,
    max_value=10000,
    value=1000
)

if st.button("Predict"):

    prediction = model.predict([[size]])

    st.write(f"Predicted price: ₹{prediction[0]:.2f} lakh")