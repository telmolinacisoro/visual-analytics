import streamlit as st

st.title("Session state")

st.write("st.session_state object:", st.session_state)

if "a_counter" not in st.session_state:
    st.session_state["a_counter"] = 0
if "boolean" not in st.session_state:
    st.session_state["boolean"] = False

st.write(st.session_state)
st.write("a_counter is", st.session_state["a_counter"])

for key, value in st.session_state.items():
    st.write(key, value)

button = st.button("Update state")

st.write("Before pressing button:", st.session_state)

if button:
    st.session_state["a_counter"] += 1
    st.write("The a_counter now is taking the value:", st.session_state["a_counter"])