import os
import joblib
import numpy as np

# Path to the saved model pipeline
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.joblib')

# Load the trained model pipeline (includes scaler + model)
model = joblib.load(MODEL_PATH)

def predict_glucose(features):
    """
    Predict glucose level using pre-averaged sensor features (50 values).
    :param features: List of 50 preprocessed (averaged) values
    :return: Predicted glucose level (float)
    """
    if len(features) != 50:
        raise ValueError(f"Expected 50 averaged features. Got {len(features)}.")

    prediction = model.predict([features])  # Ensure 2D input
    return float(prediction[0])
