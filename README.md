# Student Score Predictor

Machine Learning project that predicts student exam scores based on:

- Hours Studied
- Attendance
- Previous Score

## Tech Stack

- Python
- Scikit-learn
- FastAPI
- Streamlit

## Run

### Train Model

python training/train.py

### Start Backend

uvicorn backend.app:app --reload

### Start Frontend

streamlit run frontend/streamlit_app.py
