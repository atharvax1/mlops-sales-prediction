from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
@app.route("/")
def home():
    return "MLOps Sales Prediction API is running"
def predict():
    data = request.json
    features = np.array(data["features"]).reshape(1, -1)
    
    prediction = model.predict(features)
    
    return jsonify({"sales_prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
