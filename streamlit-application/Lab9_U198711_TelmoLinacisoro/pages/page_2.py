import streamlit as st
import time

def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(10)  
    return a * b + 1

a, b = 3, 210
res = expensive_computation(a, b)
st.write("Result:", res)

@st.cache_data()
def expensive_computation_2(a, b):
    st.write("Cache miss: expensive_computation_2(", a, ",", b, ") ran")
    time.sleep(10)  
    return a * b + 1

res_cached = expensive_computation_2(a, b)
st.write("Result with caching:", res_cached)

@st.cache_data()
def expensive_computation_3(a, b):
    st.write("Cache miss: expensive_computation_3(", a, ",", b, ") ran")
    time.sleep(5)  
    return a * b

a = 2
b = st.slider("Pick a number", 0, 10)
res_slider = expensive_computation_3(a, b)
st.write("Result with slider:", res_slider)

st.title('Counter Example using Callbacks with args')

if 'count' not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input('Enter a value to increment by', value=0, step=1)

def increment_counter(increment_value):
    st.session_state.count += increment_value

increment = st.button('Increment', on_click=increment_counter, args=(increment_value,))

st.write('Count =', st.session_state.count)