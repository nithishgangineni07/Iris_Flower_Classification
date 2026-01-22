import joblib  # to load the trained model
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

# Flask to create API endpoint
app = Flask(__name__)
CORS(app)

# Load the trained model (Random Forest Pipeline)
model = joblib.load("iris_random_forest_model.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    """
    API endpoint to get the data from the Streamlit app
    and return the predicted iris species
    """

    data = request.json  # get data from Streamlit app

    # Convert input data into a pandas DataFrame
    input_df = pd.DataFrame([{
        "sepal_length": data["sepal_length"],
        "sepal_width": data["sepal_width"],
        "petal_length": data["petal_length"],
        "petal_width": data["petal_width"]
    }])

    # Make prediction
    prediction = model.predict(input_df)
   

    # Return prediction to Streamlit
    return jsonify({
        "predicted_species": prediction[0],
       
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
