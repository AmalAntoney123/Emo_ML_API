from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the model and scaler
with open('mood_model.pkl', 'rb') as f:
    model, scaler = pickle.load(f)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([
        data['sleep_quality'],
        data['stress_level'],
        data['physical_activity'],
        np.sin(2 * np.pi * data['day_of_week'] / 7),
        np.cos(2 * np.pi * data['day_of_week'] / 7)
    ]).reshape(1, -1)

    # Scale the features
    scaled_features = scaler.transform(features)

    # Make prediction
    prediction = model.predict(scaled_features)[0]

    return jsonify({'predicted_mood': round(prediction, 1)})

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200