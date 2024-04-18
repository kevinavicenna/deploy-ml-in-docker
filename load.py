import streamlit as st
import matplotlib.pyplot as plt
import requests
import json
import numpy as np
from tensorflow.keras.datasets.mnist import load_data

# Load MNIST dataset
(_, _), (x_test, y_test) = load_data()
# Reshape data to have a single channel
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], x_test.shape[2], 1))
# Normalize pixel values
x_test = x_test.astype('float32') / 255.0

# Server URL
url = 'http://localhost:8501/v1/models/img_classifier:predict'

# Function to make predictions
def make_prediction(instances):
    data = json.dumps({"signature_name": "serving_default", "instances": instances.tolist()})
    headers = {"content-type": "application/json"}
    json_response = requests.post(url, data=data, headers=headers)
    predictions = json.loads(json_response.text)['predictions']
    return predictions

# Get predictions for the first 4 images
predictions = make_prediction(x_test[0:4])

# Display predictions in Streamlit app
st.title('MNIST Image Classifier Predictions')
for i, pred in enumerate(predictions):
    st.write(f"True Value: {y_test[i]}, Predicted Value: {np.argmax(pred)}")
