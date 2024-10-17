import streamlit as st
import requests

st.title("Scholarship Prediction")

feature1 = st.number_input("Feature 1", min_value=0.0, max_value=1.0, step=0.01)
feature2 = st.number_input("Feature 2", min_value=0.0, max_value=1.0, step=0.01)
feature3 = st.number_input("Feature 3", min_value=0.0, max_value=1.0, step=0.01)

if st.button("Predict"):
    response = requests.post("http://127.0.0.1:8000/predict", json={
        "feature1": feature1,
        "feature2": feature2,
        "feature3": feature3
    })
    prediction = response.json()
    st.write(f"Prediction: {prediction['prediction']}")
