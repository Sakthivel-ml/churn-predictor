import streamlit as st
import numpy as np
import pickle

# Load the model and scaler
with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("📉 Customer Churn Prediction App")

# User input form
with st.form("churn_form"):
    gender = st.selectbox("Gender", ['Male', 'Female'])
    senior_citizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
    partner = st.selectbox("Partner", ['Yes', 'No'])
    dependents = st.selectbox("Dependents", ['Yes', 'No'])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
    multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
    contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
    paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
    payment_method = st.selectbox("Payment Method", [
        'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
    ])
    monthly_charges = st.number_input("Monthly Charges", value=70.0)
    total_charges = st.number_input("Total Charges", value=2000.0)

    submit = st.form_submit_button("Predict")

# Input encoding (must match training)
def encode_input():
    return np.array([[
        1 if gender == 'Male' else 0,
        1 if senior_citizen == 'Yes' else 0,
        1 if partner == 'Yes' else 0,
        1 if dependents == 'Yes' else 0,
        tenure,
        1 if phone_service == 'Yes' else 0,
        0 if multiple_lines == 'No' else 1 if multiple_lines == 'Yes' else 2,
        {'DSL': 0, 'Fiber optic': 1, 'No': 2}[internet_service],
        {'Yes': 0, 'No': 1, 'No internet service': 2}[online_security],
        {'Yes': 0, 'No': 1, 'No internet service': 2}[online_backup],
        {'Yes': 0, 'No': 1, 'No internet service': 2}[device_protection],
        {'Yes': 0, 'No': 1, 'No internet service': 2}[tech_support],
        {'Yes': 0, 'No': 1, 'No internet service': 2}[streaming_tv],
        {'Yes': 0, 'No': 1, 'No internet service': 2}[streaming_movies],
        {'Month-to-month': 0, 'One year': 1, 'Two year': 2}[contract],
        1 if paperless_billing == 'Yes' else 0,
        {'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3}[payment_method],
        monthly_charges,
        total_charges
    ]])

# Predict and display
if submit:
    X_input = encode_input()
    X_scaled = scaler.transform(X_input)
    prediction = model.predict(X_scaled)[0]
    st.write("Raw prediction (0 = No Churn, 1 = Churn):", prediction)
    result = "🔴 Customer is likely to churn." if prediction == 1 else "🟢 Customer is not likely to churn."
    st.success(result)
