import streamlit as st
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import os
import shap

# Page Configuration
st.set_page_config(page_title="Global Explainability", layout="wide")

# Page Title and Introduction
st.title("Global Explainability for Acute Pancreatitis Predictions")
st.markdown("""
In here we provide some visualizations to understand the prediction of the model. Hopefully this is helpful!! 🤗
""")

# Function to display an image with error handling
def display_image(file_path, caption):
    if os.path.exists(file_path):
        st.image(file_path, caption=caption, use_column_width=True)
    else:
        st.error(f"File not found: {file_path}")

# Function to load the pre-trained model
@st.cache_resource
def load_model():
    with open("OF_PERSIS_ANYTIME_classification_model.pkl", "rb") as file:
        return pickle.load(file)
model = load_model()

# Load and preprocess test data
df = pd.read_csv('Stage_2.csv', sep=";")
X_test = df.drop(columns=['OF_PERSIS_ANYTIME', 'ID_PATIENT'])  # Drop irrelevant columns
y_test = df['OF_PERSIS_ANYTIME']

# Create SHAP explainer
explainer = shap.Explainer(model)
shap_values = explainer(X_test)

# Feature Importance
st.markdown("## Feature Importance")
st.markdown("What's the overall importance of each feature in the model? 🧐")
display_image("./Images/importance_of_feature.png", "Feature Importance Bar Plot")

# Bar plot for top 15 features
st.markdown("### Bar Plot for Top 15 Features")
fig_bar = plt.figure()  # Create a new figure for the bar plot
num_features = 15
shap.plots.bar(shap_values[:, :, 1], max_display=num_features+1, show=False)
st.pyplot(fig_bar)  # Pass the figure to st.pyplot()

# Summary plot
st.markdown("###  Summary Plot")
fig_summary = plt.figure()  # Create a new figure for the summary plot
shap.summary_plot(shap_values[:, :, 1], X_test, show=False)
st.pyplot(fig_summary)  # Pass the figure to st.pyplot()

# SHAP Scatter Plots
st.markdown("## SHAP Scatter Plots")
st.markdown("Scatter plots show the relationship between specific features and their SHAP values.")
display_image("./Images/scatter_heartrate.png", "SHAP Scatter Plot for Heart Rate")
display_image("./Images/scatter_age.png", "SHAP Scatter Plot for Age")
display_image("./Images/scatter_satofio.png", "SHAP Scatter Plot for Oxygen Saturation/FiO2")

selected_feature = st.selectbox(
    "Select Feature to Visualize",
    X_test.columns,
    index=X_test.columns.get_loc("AGE") if "AGE" in X_test.columns else 0
)

st.markdown(f"### Scatter Plot for {selected_feature}")
fig_scatter = plt.figure()  # Create a new figure for the scatter plot
shap.plots.scatter(shap_values[:, X_test.columns.get_loc(selected_feature), 1], show=False)
st.pyplot(fig_scatter)  # Pass the figure to st.pyplot()