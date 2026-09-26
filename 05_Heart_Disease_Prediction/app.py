import streamlit as st
import pandas as pd
import joblib


# ==============================
# LOAD SAVED FILES
# ==============================

model = joblib.load("Logis_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")


# ==============================
# TITLE
# ==============================

st.title("Heart Disease Prediction ❤️")

st.markdown("Provide the following details")


# ==============================
# USER INPUTS
# ==============================

age = st.slider(
    "Age",
    18,
    100,
    40
)

sex = st.selectbox(
    "Sex",
    ["M", "F"]
)

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "TA", "ASY"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure",
    80,
    200,
    120
)

cholesterol = st.number_input(
    "Cholesterol",
    100,
    600,
    200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.slider(
    "Max Heart Rate",
    60,
    220,
    150
)

exercise_angina = st.selectbox(
    "Exercise-Induced Angina",
    ["Y", "N"]
)

oldpeak = st.slider(
    "Oldpeak (ST Depression)",
    0.0,
    6.0,
    1.0
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)


# ==============================
# PREDICT BUTTON
# ==============================

if st.button("Predict"):

    # --------------------------
    # Create input dictionary
    # --------------------------

    raw_input = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,

        "Sex_M": 1 if sex == "M" else 0,

        "ChestPainType_ATA": 1 if chest_pain == "ATA" else 0,
        "ChestPainType_NAP": 1 if chest_pain == "NAP" else 0,
        "ChestPainType_TA": 1 if chest_pain == "TA" else 0,

        "RestingECG_Normal": 1 if resting_ecg == "Normal" else 0,
        "RestingECG_ST": 1 if resting_ecg == "ST" else 0,

        "ExerciseAngina_Y": 1 if exercise_angina == "Y" else 0,

        "ST_Slope_Flat": 1 if st_slope == "Flat" else 0,
        "ST_Slope_Up": 1 if st_slope == "Up" else 0
    }


    # --------------------------
    # Convert to DataFrame
    # --------------------------

    input_df = pd.DataFrame([raw_input])


    # --------------------------
    # Make sure columns are
    # in correct order
    # --------------------------

    input_df = input_df[expected_columns]


    # --------------------------
    # Scale ONLY numerical columns
    # --------------------------

    numerical_columns = scaler.feature_names_in_

    input_df[numerical_columns] = scaler.transform(
        input_df[numerical_columns]
    )


    # --------------------------
    # Make final prediction
    # --------------------------

    prediction = model.predict(input_df)[0]


    # --------------------------
    # Display result
    # --------------------------

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")

    else:
        st.success("✅ Low Risk of Heart Disease")