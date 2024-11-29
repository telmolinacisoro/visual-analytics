import streamlit as st
import numpy as np
import pandas as pd
import pickle
import shap
import os
import matplotlib.pyplot as plt

# Load the trained model and create SHAP explainer
@st.cache_resource
def load_model_and_explainer():
    # Load the model
    with open("OF_PERSIS_ANYTIME_classification_model.pkl", "rb") as file:
        model = pickle.load(file)
    
    # Load training data
    df = pd.read_csv("C:\\Users\\telmo.linacisoro\\Downloads\\Lab11_U198711_TelmoLinacisoro\\Stage_2.csv", sep=";")
    
    # Prepare background data for SHAP explainer
    X_train = df.drop('OF_PERSIS_ANYTIME', axis=1)
    
    # Create SHAP explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_train,check_additivity=False)
    
    return model, explainer

# Load the model and SHAP explainer
model, explainer = load_model_and_explainer()

# Load the trained model
@st.cache_resource
def load_model():
    with open("OF_PERSIS_ANYTIME_classification_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def display_image(file_path):
    if os.path.exists(file_path):
        st.image(file_path, use_column_width=True)
    else:
        st.error(f"File not found: {file_path}")

# Ensure input data matches the feature set used for training
def prepare_input_data(patient_data, feature_columns):
    """
    Matches patient data with the full feature set required by the model.
    Fills missing features with 0 or appropriate default values.
    """
    feature_columns = [col for col in feature_columns if col != 'OF_PERSIS_ANYTIME']

    # Convert the input to a DataFrame
    input_df = pd.DataFrame([patient_data])

    # Ensure all feature columns are present and handle missing features
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0  # Default value for missing features

    # Reorder columns to match the expected order
    input_df = input_df[feature_columns]

    return input_df

# Prediction function
def predict_persistent_failure(patient_data, model, feature_columns):
    """
    Predicts the likelihood of persistent organ failure.
    """
    patient_df = prepare_input_data(patient_data, feature_columns)
    patient_array = patient_df.values  # Convert to numpy array
    prediction = model.predict(patient_array)[0]  # Class prediction
    prob = model.predict_proba(patient_array)[0, 1]  # Probability for class 1
    return prediction, prob, patient_df

# Streamlit app
st.title("Predict Persistent Organ Failure")

# Load the model and feature columns
model = load_model()
feature_columns = [
    "BMI", "AGE", "ALCOHOL_UNITS_WEEK", "ALCOHOLCOM", "ALCOHOLYEA", "YEARABSTIN", "ASA",
    "BACTERIALI", "COLICBEFOR", "HTA", "CARDIO", "DIABETESAP", "DIABETESNE", "DYSLIPID",
    "RESP_PREVIOUSDISEA", "RENALCRONI", "FAMILIARCA", "FAMILIAR_A", "GENEALTERA",
    "HISTORY_CHOLECYSTECTOMY", "HEREDPANCR", "NUMBERPREV", "PREVIOUS_A", "PARASITINF",
    "PCRONICAETIOLOGY", "PACKYEAR", "CIGARRETEP", "SMOKINGYEA", "STONESHIST", "TRYGLICERI",
    "VIRUSTYPE", "ETIOLOGYFI", "IPMN_global", "OF_PERSIS_ANYTIME", "ANTIARRITMICO",
    "ANTIINFLAMATORIO", "BETABLOQUEANTES", "DIURETICO", "IECA", "ANTICOAGULANTE",
    "ANTIPLAQUETARIO", "ANTIDIABETICO", "ESTATINA", "BRONCODILATADORES", "ANTIDEPRESIVOS",
    "HOURSADMISSPAIN", "APCRITER_A", "GLASGOWMENTAL", "TEMPEAPACHE_ADMISS", "PAM_ADMISS",
    "HEARTRATED_ADMISS", "RESPFREQUE_ADMISS", "SATO2%/FIO2%_ADMISS", "SEX"
]

# Input fields for user data
st.subheader("Input Patient Data")
patient_data = {
    "BMI": st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1),
    "AGE": st.number_input("Age", min_value=0, max_value=120, step=1),
    "ALCOHOL_UNITS_WEEK": st.number_input("Alcohol Units per Week", min_value=0, max_value=100, step=1),
    "HTA": st.selectbox("Hypertension (HTA)", [0, 1]),
    "CARDIO": st.selectbox("Cardiovascular Disease", [0, 1]),
    "DIABETESAP": st.selectbox("Diabetes (Acute Pancreatitis)", [0, 1]),
    "SEX": st.selectbox("Sex", [0, 1]),  # Replace with appropriate encoding (e.g., 0 for Male, 1 for Female)
}

# Modify the predict button section to include SHAP explanation
if st.button("Predict"):
    prediction, probability, input_df = predict_persistent_failure(patient_data, model, feature_columns)
    outcome = "Persistent Failure" if prediction == 1 else "No Persistent Failure"
    st.write(f"### Prediction: {outcome}")
    st.write(f"### Probability of Persistent Failure: {probability:.2%}")
    
    # Add SHAP Explanation
    st.subheader("Model Explanation")
    
    # Prepare input for SHAP
    shap_input = prepare_input_data(patient_data, feature_columns)
    
    # Calculate SHAP values
    shap_values = explainer(shap_input)
    
    # Waterfall Plot
    st.write("#### Feature Impact Waterfall Plot")
    fig, ax = plt.subplots(figsize=(10, 6))
    shap.plots.waterfall(shap_values[0, :, 0], max_display=10)
    st.pyplot(fig)
    plt.close(fig)
    
    # Decision Plot
    # st.write("#### Decision Plot")
    # fig, ax = plt.subplots(figsize=(12, 6))
    # shap.decision_plot(
    #     explainer.expected_value[0],  
    #     shap_values[0, :, 0],  
    #     shap_input.columns, 
    #     link='logit'
    # )
    
    st.write("#### Decision Plot") # This is just an example because the code above wasn't working... sorry I couldn't get it to work with the limited time 
    display_image("./Images/decision_plot.png")