import streamlit as st
import numpy as np
import joblib
import os

# -------------------------------
# Load Model (UPDATED PATH)
# -------------------------------
MODEL_PATH = os.path.join(
    "Backend", "iris_random_forest_model.pkl"
)

model = joblib.load(MODEL_PATH)

# -------------------------------
# UI
# -------------------------------
st.title("🌸 IRIS FLOWER SPECIES PREDICTION")
st.write("Please enter the details to get the flower species")

# -------------------------------
# Input Sliders
# -------------------------------
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.3)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):

    input_data = np.array([
        [sepal_length, sepal_width, petal_length, petal_width]
    ])

    prediction = model.predict(input_data)[0]

    # Model already returns label like "setosa"
    st.success(f"🌼 Predicted Species: **Iris-{prediction.capitalize()}**")
