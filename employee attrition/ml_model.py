import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import warnings

warnings.filterwarnings("ignore")

MODEL_FILENAME = "attrition_model.pkl"

def train_model(csv_file):
    if not os.path.exists(csv_file):
        raise Exception("Data file not found.")

    data = pd.read_csv(csv_file)

    if data.shape[0] < 5:
        raise Exception("Not enough data to train. Add more employee records.")

    X = data[['experience', 'salary', 'workload']]
    y = data['attrition']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    joblib.dump(model, MODEL_FILENAME)

def predict_attrition(experience, salary, workload):
    if not os.path.exists(MODEL_FILENAME):
        raise Exception("Model not found. Train the model first.")

    model = joblib.load(MODEL_FILENAME)
    input_data = [[experience, salary, workload]]
    prediction = model.predict(input_data)[0]
    return prediction
