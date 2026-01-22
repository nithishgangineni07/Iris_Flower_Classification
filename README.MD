# 🌸 Iris Flower Prediction App

This project is a machine learning web application that predicts the species of an Iris flower based on user-provided measurements. The model is built using a Random Forest Classifier, and the frontend interface is developed using Streamlit.

---

## 📌 Project Overview

The Iris dataset is a classic dataset used in machine learning and contains flower measurements for three species:
- Iris Setosa
- Iris Versicolor
- Iris Virginica

The application takes the following inputs:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Based on these values, the trained model predicts the flower species.

---

## 🧠 Model Details

- Algorithm: Random Forest Classifier  
- ML Library: scikit-learn  
- Model Training: Python  
- Model File: `iris_random_forest.pkl`

---

## 🖥️ Tech Stack

Backend:
- Python
- scikit-learn
- pandas
- numpy
- joblib / pickle

Frontend:
- Streamlit

---

## 📂 Project Structure

```
Iris/
│
├── Backend/
│   ├── data/
│   │   └── load_data.py
│   ├── model/
│   │   ├── train_model.py
│   │   ├── train_save.py
│   │   └── iris_random_forest.pkl
│   ├── app.py
│   └── requirements.txt
│
├── Frontend/
│   ├── app.py
│   └── requirements.txt
│
├── iris_env/
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/iris-flower-prediction.git
cd iris-flower-prediction
```

### 2️⃣ Create a Virtual Environment (Optional)
```bash
python -m venv iris_env
source iris_env/bin/activate   # Linux / Mac
iris_env\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

Or install separately:
```bash
pip install -r Backend/requirements.txt
pip install -r Frontend/requirements.txt
```

---

## 🏋️ Train the Model
```bash
python Backend/model/train_save.py
```

This script trains the Random Forest model and saves it for later use.

---

## 🌐 Run the Streamlit App
```bash
streamlit run Frontend/app.py
```

Then open your browser and visit:
```
http://localhost:8501
```

---

## 🎯 Features

- Interactive Streamlit UI
- Real-time Iris flower prediction
- Accurate Random Forest model
- Clean and modular project structure

---

## 📊 Sample Input

| Feature        | Value |
|---------------|-------|
| Sepal Length  | 5.1   |
| Sepal Width   | 3.5   |
| Petal Length  | 1.4   |
| Petal Width   | 0.2   |

Prediction Output:
```
Iris-setosa
```

---

⭐ If you find this project useful, please consider giving it a star!