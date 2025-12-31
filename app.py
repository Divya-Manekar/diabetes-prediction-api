from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load dataset (must be in same folder)
try:
    df = pd.read_csv("diabetes.csv")
except Exception as e:
    df = None
    print("Error loading dataset:", e)

@app.route("/")
def home():
    return "API is running"

@app.route("/predict", methods=["POST"])
def predict():
    if df is None:
        return jsonify({"error": "Dataset not loaded"}), 500

    data = request.json

    try:
        glucose = float(data.get("Glucose", 0))
        bmi = float(data.get("BMI", 0))
        age = float(data.get("Age", 0))
    except Exception:
        return jsonify({"error": "Invalid input"}), 400

    # Simple rule-based logic (replace with ML later)
    if glucose > 140 and bmi > 30:
        prediction = "Diabetic"
    else:
        prediction = "Non-Diabetic"

    return jsonify({
        "prediction": prediction,
        "input": {
            "Glucose": glucose,
            "BMI": bmi,
            "Age": age
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
