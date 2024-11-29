import streamlit as st

# Configure the page
st.set_page_config(page_title="Acute Pancreatitis Prediction", layout="wide")

# Main Title and Introduction
st.title("Acute Pancreatitis Prediction and Explainability")
st.subheader("Welcome to the Acute Pancreatitis Analysis and Prediction App! 🚑")

st.markdown("""
This app is designed to help medical professionals explore patient data, predict outcomes, and interpret predictions for Acute Pancreatitis cases.
- **Explore** visualizations of patient data to gain insights 📊
- **Predict** the likelihood of persistent organ failure for a new patient case and deeper insights into the local explainability 🧐
- **Global Explainability** the global behavior of the model and how it makes predictions 🔍
   
👈🏻 Use the sidebar to navigate through the application!
""")


st.image("./Images/organ.jpeg", use_column_width=True)
