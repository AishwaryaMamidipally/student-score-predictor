import streamlit as st
import requests
st.title("Students Score Predictor")
hours = st.number_input("Hours Studied", min_value=0.0)
attendance = st.number_input(
    "Attendance %",
    min_value=0.0,
    max_value=100.0
)
previous = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0
)
if st.button("Predict"):
    payload={
        "hours_studied": hours,
        "attendance": attendance,
        "previous_score": previous
    }
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )
    result = response.json()
    st.success(
        f"Predicted Exam Score: {result['prediction_score']}"
    )