import joblib
import pandas as pd

model = joblib.load("backend/model.pkl")

def predict_score(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return float(prediction)