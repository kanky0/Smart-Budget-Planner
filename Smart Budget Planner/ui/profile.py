import streamlit as st
from utils.state import next_step

def render():
    st.header("Profile")

    age = st.slider("Age", 15, 70, 22)
    status = st.radio("Current Status", ["Student", "Working"])

    st.session_state.profile = {
        "Age": age,
        "Status": status
    }

    st.caption("Age and status influence cost patterns")

    if st.button("Next"):
        next_step()
