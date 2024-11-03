import streamlit as st

st.title("Session state")

# Display the session state object for reference
st.write("st.session_state object:", st.session_state)

# Initialization
if "a_counter" not in st.session_state:
    st.session_state["a_counter"] = 0
if "boolean" not in st.session_state:
    st.session_state["boolean"] = False

# Display session state and current value of a_counter
st.write(st.session_state)
st.write("a_counter is", st.session_state["a_counter"])

# Display each item in session_state
for key, value in st.session_state.items():
    st.write(key, value)

# Button to update state
button = st.button("Update state")

# Display state before pressing the button
st.write("Before pressing button:", st.session_state)

# Update a_counter if button is pressed
if button:
    st.session_state["a_counter"] += 1
    st.write("The a_counter now is taking the value:", st.session_state["a_counter"])