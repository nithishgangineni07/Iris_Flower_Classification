import streamlit as st
import requests

st.title("🌸 IRIS FLOWER SPECIES PREDICTION")
st.write("Please enter the details to get the flower species")

# Input fields
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.3)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

if st.button("Predict"):

    # JSON data to send to Flask API
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    # Call Flask backend
    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json=input_data
    )

    if response.status_code == 200:
        result = response.json()
        prediction = result["predicted_species"]
      

        st.success(f"🌼 Predicted Species: **{prediction}**")
        
    else:
        st.error("❌ Error in prediction. Is the backend running?")
