# ml_utils/ml_model.py
import os
import joblib
import numpy as np
import pandas as pd

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

    # Ensure the input is a DataFrame with proper column names
    labels = ['white', 'red', 'ir', 'green', 'none']
    column_names = [f'{label}{i+1}' for label in labels for i in range(10)]
    input_df = pd.DataFrame([features], columns=column_names)

    prediction = model.predict(input_df)
    return float(prediction[0])
