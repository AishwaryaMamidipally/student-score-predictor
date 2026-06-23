import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

df = pd.read_csv("data/students.csv")

X = df[["hours_studied", "attendance", "previous_score"]]
y = df["exam_score"]

model = LinearRegression()

model.fit(X, y)

os.makedirs("backend", exist_ok=True)

joblib.dump(model, "backend/model.pkl")

print("Model trained and saved!")