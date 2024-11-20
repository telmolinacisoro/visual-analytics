import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from data_processing import load_and_clean_data
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Explore Software Engineer Salaries")

df = load_and_clean_data() # The data is loaded and cleaned in the same way as in the EDA notebook, another option would've been to directly download the updated dataframe as a csv, but this works as well

# Number of Data Points by Country
st.markdown("### Number of Data Points by Country")
country_counts = df['Country'].value_counts(normalize=True) * 100
# Explode effect for smaller sections
explode = [0.1 if country_counts[country] < 5 else 0 for country in country_counts.index]
fig1, ax1 = plt.subplots()
colors = plt.get_cmap("Spectral")(np.linspace(0, 1, len(country_counts)))
wedges, texts, autotexts = ax1.pie(
    country_counts,
    explode=explode,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 10, 'weight': 'bold'}
)
# Rotation adjustment to make it readable
for autotext, wedge in zip(autotexts, wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
    autotext.set_rotation(angle - 180 if angle <= 250 else angle - 360)
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')
plt.legend(country_counts.index, title="Country", loc="center left", bbox_to_anchor=(1, 0.5), fontsize='small')
st.pyplot(fig1)

# Mean Salary by Country Bar Plot
st.markdown("### Mean Salary by Country")
mean_salary_country = df.groupby("Country")["Salary"].mean().sort_values()
fig2, ax2 = plt.subplots(figsize=(10, 8))
colors = sns.color_palette("coolwarm", len(mean_salary_country))
sns.barplot(x=mean_salary_country.index, y=mean_salary_country.values, palette=colors, ax=ax2)
for i, (country, salary) in enumerate(zip(mean_salary_country.index, mean_salary_country.values)):
    font_size = 10 if len(country) <= 10 else 8 if len(country) <= 15 else 6
    ax2.text(i, salary * 0.5, country, ha='center', va='center', rotation=90, color='white', weight='bold', fontsize=font_size)
ax2.set_xticklabels([])  # We remove x-tick labels because we introduced them in the bars themselves
st.pyplot(fig2)

# Mean Salary by Country Map
st.markdown("### World Map Mean Salary by Country")
shapefile_path = r"C:\Users\telmo.linacisoro\OneDrive - Accenture\Documents\Lab10_U198711_TelmoLinacisoro\ne_10m_admin_0_countries.shp" # Got this from the internet https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/
world = gpd.read_file(shapefile_path)
mean_salary_country = df.groupby("Country")["Salary"].mean()
# Merge the geospatial data with the salary data
world = world.rename(columns={'ADMIN': 'Country'})
world = world.set_index('Country').join(mean_salary_country).reset_index()
fig, ax = plt.subplots(figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1, color='black')
world.plot(column='Salary', ax=ax, legend=True,
           legend_kwds={'label': "Average Salary by Country (USD)",
                        'orientation': "horizontal"},
           cmap='coolwarm')
st.pyplot(fig)

# Salary Distribution by Country
st.markdown("### Salary Distribution by Country")
fig7, ax7 = plt.subplots(figsize=(12, 8))
sns.boxplot(data=df, x='Salary', y='Country', palette=colors, fliersize=2, ax=ax7)
ax7.set_xlabel("Salary (USD)")
ax7.set_ylabel("Country")
st.pyplot(fig7)

# Mean Salary by Years of Experience
st.markdown("### Mean Salary by Years of Experience")
mean_salary_experience = df.groupby("YearsCodePro")["Salary"].mean()
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.lineplot(x=mean_salary_experience.index, y=mean_salary_experience.values, marker='o', ax=ax3, label="Mean Salary")
# Regression line
x_exp = mean_salary_experience.index.values.reshape(-1, 1)
y_exp = mean_salary_experience.values
regressor_exp = LinearRegression().fit(x_exp, y_exp)
y_pred_exp = regressor_exp.predict(x_exp)
ax3.plot(mean_salary_experience.index, y_pred_exp, color='red', linewidth=2, linestyle='--', label="Regression Line")
ax3.set_xlabel("Years of Experience")
ax3.set_ylabel("Mean Salary (USD)")
ax3.legend()
st.pyplot(fig3)

# Salary Distribution by Education Level
st.markdown("### Salary Distribution by Education Level")
fig8, ax8 = plt.subplots(figsize=(8, 6))
sns.violinplot(data=df, x='EdLevel', y='Salary', color="lightblue", ax=ax8)
ax8.set_xlabel("Education Level")
ax8.set_ylabel("Salary (USD)")
st.pyplot(fig8)