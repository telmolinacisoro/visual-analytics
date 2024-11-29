import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page Configuration
st.set_page_config(page_title="Acute Pancreatitis Patient Data Exploration", layout="wide")

# Page Title
st.title("Explore Acute Pancreatitis Patient Data")

# Load the dataset
df = pd.read_csv("C:\\Users\\telmo.linacisoro\\Downloads\\Lab11_U198711_TelmoLinacisoro\\Stage_2.csv", sep=";")

# Sidebar Filters
st.sidebar.header("Filters")
age_range = st.sidebar.slider("Select Age Range", int(df["AGE"].min()), int(df["AGE"].max()), (30, 60))
bmi_range = st.sidebar.slider("Select BMI Range", int(df["BMI"].min()), int(df["BMI"].max()), (20, 30))

# Apply Filters
filtered_df = df[(df["AGE"] >= age_range[0]) & (df["AGE"] <= age_range[1]) &
                 (df["BMI"] >= bmi_range[0]) & (df["BMI"] <= bmi_range[1])]

# Distribution of BMI with Filters
st.markdown("### What is the BMI distribution for the selected age?")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df["BMI"], kde=True, color="skyblue", ax=ax1)
ax1.set_title("BMI Distribution")
ax1.set_xlabel("BMI")
st.pyplot(fig1)

# Age Distribution with Filters
st.markdown("### What is the age distribution for the selected BMI?")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df["AGE"], kde=True, color="orange", ax=ax2)
ax2.set_title("Age Distribution")
ax2.set_xlabel("Age")
st.pyplot(fig2)

# Persistent Organ Failure Outcome
st.markdown("### Outcome of Persistent Organ Failure")
fig3, ax3 = plt.subplots()
outcome_counts = filtered_df["OF_PERSIS_ANYTIME"].value_counts(normalize=True) * 100
outcome_counts.plot.pie(
    autopct="%1.1f%%",
    colors=["#ff9999", "#66b3ff"],
    labels=["No Persistent Failure", "Persistent Failure"],
    ax=ax3,
    startangle=90
)
ax3.set_ylabel("")
ax3.set_title("Persistent Organ Failure Outcomes")
st.pyplot(fig3)

# Dynamic Scatterplot: Age vs BMI
st.markdown("### Age vs BMI")
color_option = st.selectbox("You can choose to color the plots by:", ["OF_PERSIS_ANYTIME", "SEX", "SMOKINGYEA"])
fig4, ax4 = plt.subplots()
sns.scatterplot(data=filtered_df, x="AGE", y="BMI", hue=color_option, ax=ax4, palette="Set2")
ax4.set_title("Age vs BMI")
ax4.set_xlabel("Age")
ax4.set_ylabel("BMI")
st.pyplot(fig4)

# Correlation Heatmap
st.markdown("### Correlation Heatmap")
fig5, ax5 = plt.subplots(figsize=(16, 12))
corr = filtered_df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax5)
ax5.set_title("Feature Correlation Heatmap")
st.pyplot(fig5)

# Alcohol Units per Week Distribution
st.markdown("### Alcohol Units per Week Distribution")
fig6, ax6 = plt.subplots()
sns.histplot(filtered_df["ALCOHOL_UNITS_WEEK"], kde=True, color="purple", ax=ax6)
ax6.set_title("Alcohol Units per Week Distribution")
ax6.set_xlabel("Alcohol Units per Week")
st.pyplot(fig6)

# Comparison: Alcohol Units per Week vs Persistent Organ Failure
st.markdown("### Alcohol Units per Week vs Persistent Organ Failure")
fig7, ax7 = plt.subplots()
sns.boxplot(data=filtered_df, x="OF_PERSIS_ANYTIME", y="ALCOHOL_UNITS_WEEK", palette=["#ff9999", "#66b3ff"], ax=ax7)
ax7.set_xticklabels(["No Persistent Failure", "Persistent Failure"])
ax7.set_title("Alcohol Units per Week by Outcome")
ax7.set_xlabel("Outcome")
ax7.set_ylabel("Alcohol Units per Week")
st.pyplot(fig7)

st.markdown("""(Key takeawy: don't drink too much alcohol... 🥴🍻)""")
