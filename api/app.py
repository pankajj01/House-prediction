from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Load the model and scaler
MODEL_PATH = '/Users/Pankaj/Desktop/Assesment/models/best_model.pkl'
SCALER_PATH = '/Users/Pankaj/Desktop/Assesment/models/scaler.pkl'


# Load saved model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Define feature names (ensure the order matches what the model was trained on)
FEATURE_NAMES = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 
                  'AveOccup', 'Latitude', 'Longitude']

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint to predict housing prices based on input features"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input features
        for feature in FEATURE_NAMES:
            if feature not in data:
                return jsonify({"error": f"Missing feature: {feature}"}), 400
        
        # Extract features in correct order
        features = [data[feature] for feature in FEATURE_NAMES]
        
        # Convert to numpy array and reshape for single sample
        features_array = np.array(features).reshape(1, -1)
        
        # Scale features
        scaled_features = scaler.transform(features_array)
        
        # Make prediction
        prediction = model.predict(scaled_features)[0]
        
        # Return prediction (price in $100k)
        return jsonify({"predicted_price": float(prediction)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)