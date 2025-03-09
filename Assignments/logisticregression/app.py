import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained logistic regression model
model = joblib.load('logistic_model.pkl')

st.title("Titanic Survival Prediction")

# User inputs for features
pclass = st.selectbox("Passenger Class", [1,2,3])
age = st.slider("Age", 0, 100, 25)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=50.0)
sibsp = st.selectbox("Number of Siblings/Spouses aboard", [0,1,2,3,4,5,6,7,8])
parch = st.selectbox("Number of Parents/Children aboard", [0,1,2,3,4,5,6])
sex = st.selectbox("Gender", ["Male", "Female"])
embarked = st.selectbox("Embarked Port", ["C","Q","S"])


# Preprocess inputs to match training data format
input_data = {
    'Age_scaled': age / 100,
    'SibSp': sibsp,
    'Parch': parch,
    'Embarked_Q': 1 if embarked == "Q" else 0,
    'Embarked_S': 1 if embarked == "S" else 0,
    'Sex_male': 1 if sex == "Male" else 0,
    'Fare_scaled': fare / 600,
    'Pclass_2': 1 if pclass == 2 else 0,
    'Pclass_3': 1 if pclass == 3 else 0
}

input_df = pd.DataFrame([input_data])

# Prediction button
if st.button("Predict Survival"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.success(f"The passenger is likely to survive with probability {probability:.2f}")
    else:
        st.error(f"The passenger is unlikely to survive with probability {probability:.2f}")
