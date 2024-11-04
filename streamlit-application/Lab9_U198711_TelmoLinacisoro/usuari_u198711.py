import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import datetime
from datetime import time

st.title('This is an example of title')

st.subheader("This is an example of subheader")
st.write("This an example of sentence")

st.write("This streamlit app adds *different formats* and icons is as :sunglasses:")
st.write("This streamlit app adds *different formats* and icons is as :snow_cloud:")
st.sidebar.header("The header of the sidebar")
st.sidebar.write("*Hello*")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.write("This is line chart")
st.line_chart(chart_data)
st.write("This is the area chart")
st.area_chart(chart_data)
st.write("This is the bar chart")
st.bar_chart(chart_data)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.write("Example 1 of plot with Matplotlib")
st.pyplot(fig)

penguins = sns.load_dataset("penguins")
st.dataframe(penguins[["species", "flipper_length_mm"]].sample(6))
fig = plt.figure(figsize=(9, 7))
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plt.title("Hello Penguins!")
st.write("Example of a plot with Seaborn library")
st.pyplot(fig)

st.dataframe(penguins[["species", "flipper_length_mm"]].sample(6))

df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.write("Example of a plot with a map")
st.map(df)

x1, x2, x3 = np.random.randn(200) - 2, np.random.randn(200), np.random.randn(200) + 2
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
st.write("Example of a plot with Plotly")
st.plotly_chart(fig, use_container_width=True)