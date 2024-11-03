import streamlit as st
import time

# Step 18: Without Caching
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(10)  # This makes the function take 10s to run
    return a * b + 1

# Execute without caching
a, b = 3, 210
res = expensive_computation(a, b)
st.write("Result:", res)

# Step 19: With Caching
@st.cache_data()
def expensive_computation_2(a, b):
    st.write("Cache miss: expensive_computation_2(", a, ",", b, ") ran")
    time.sleep(10)  # This makes the function take 10s to run
    return a * b + 1

# Execute with caching
res_cached = expensive_computation_2(a, b)
st.write("Result with caching:", res_cached)

# Step 20: Slider with Cached Computation
@st.cache_data()
def expensive_computation_3(a, b):
    st.write("Cache miss: expensive_computation_3(", a, ",", b, ") ran")
    time.sleep(5)  # This makes the function take 5s to run
    return a * b

# Slider for changing the value of 'b'
a = 2
b = st.slider("Pick a number", 0, 10)
res_slider = expensive_computation_3(a, b)
st.write("Result with slider:", res_slider)

# Step 21: Session State for a Counter with Callbacks
st.title('Counter Example using Callbacks with args')

# Initialization of session state variable 'count'
if 'count' not in st.session_state:
    st.session_state.count = 0

# Input for increment value
increment_value = st.number_input('Enter a value to increment by', value=0, step=1)

# Define a callback function to increment the counter
def increment_counter(increment_value):
    st.session_state.count += increment_value

# Button to trigger the increment function
increment = st.button('Increment', on_click=increment_counter, args=(increment_value,))

# Display the current count
st.write('Count =', st.session_state.count)
