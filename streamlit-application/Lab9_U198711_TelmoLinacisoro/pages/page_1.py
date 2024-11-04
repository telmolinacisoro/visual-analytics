import streamlit as st
import datetime
from datetime import time

st.set_page_config(
    page_title="My first app with Streamlit in Visual Analytics",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://upf.edu/help',
        'Report a bug': "https://upf.edu/bug",
        'About': "# This is a header. This is *my first app*!"
    }
)

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

agree = st.checkbox('this is a checkbox')
if agree:
    st.write('Great you have clicked the checkbox!')

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary')
)
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy. You selected:", genre)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider('Select a range of values', 0.0, 100.0, value=(25.0, 75.0))
st.write('Values:', values)

appointment = st.slider("Schedule your appointment:", value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
)
st.write('My favorite color is', color)

title = st.text_input('Name of your favorite movie')
st.write('The current movie title is', title)

number = st.number_input('Insert a number')
st.write('The current number is ', number)

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)