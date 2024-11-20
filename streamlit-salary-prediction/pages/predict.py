import streamlit as st
from predictor import load_model_and_encoders, predict_salary

st.title("Predict Software Engineer Salary")
st.subheader("Input the following details to find out what the predicted salary is 🔎")

model, le_country, le_education = load_model_and_encoders()

country = st.selectbox("Country 🌍", le_country.classes_)
education = st.selectbox("Education Level 🎓", le_education.classes_)
experience = st.slider("Years of Experience 🫣", 0, 50, 5)

if st.button("Predict Salary"):
    salary_pred = predict_salary(country, education, experience, model, le_country, le_education)
    st.write(f"### Estimated Salary: ${salary_pred[0]:,.2f}")