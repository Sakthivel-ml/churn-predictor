# churn-predictor
Streamlit Churn Prediction App
# 📉 Customer Churn Prediction App

A Machine Learning-powered web application built with **Streamlit** to predict whether a telecom customer is likely to churn. This app uses a **Random Forest model** trained on the popular Telco Customer Churn dataset.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://churn-predictor-gnyex53eth4eeptarmmgg9.streamlit.app/)

---

## 🔍 Features

- Predict customer churn based on 19 features
- Clean and simple user interface using Streamlit
- Real-time predictions with results shown instantly
- Uses a trained Random Forest Classifier
- Hosted for free using Streamlit Cloud

---

## 📊 Sample Input

| Feature             | Example Value        |
|---------------------|----------------------|
| Gender              | Female               |
| Senior Citizen      | No                   |
| Tenure              | 24                   |
| Internet Service    | Fiber optic          |
| Monthly Charges     | 85.5                 |
| Contract            | Month-to-month       |
| Payment Method      | Electronic check     |

---

## ✅ Prediction Output

- 🟢 Customer is **not likely to churn**
- 🔴 Customer is **likely to churn**

---

## 🧠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Pickle (for saving models)
- GitHub + Streamlit Cloud (for hosting)

---

## 📁 Files Included

- `app.py` — Streamlit web app
- `churn_model.pkl` — Trained Random Forest model
- `scaler.pkl` — StandardScaler used for preprocessing
- `requirements.txt` — Dependencies for Streamlit Cloud

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/your-username/churn-predictor.git
cd churn-predictor
pip install -r requirements.txt
streamlit run app.py
