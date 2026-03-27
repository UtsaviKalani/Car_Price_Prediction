import streamlit as st
import requests

st.title("Car Price Predictor")

year = st.slider("Year", 2000, 2025, 2018)
km_driven = st.slider("KM Driven", 0, 200000, 30000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])

fuel = 0 if fuel_type == "Petrol" else 1

if st.button("Predict"):
    url = "http://127.0.0.1:5000/predict"

    data = {
        "year": year,
        "km_driven": km_driven,
        "fuel_type": fuel
    }

    response = requests.post(url, json=data)
    result = response.json()

    st.success(f"Estimated Price: ₹ {round(result['prediction'],2)} Lakhs")
