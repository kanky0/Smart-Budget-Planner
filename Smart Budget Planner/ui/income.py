import streamlit as st
from utils.state import next_step, prev_step

def render():
    st.header("Income")

    status = st.session_state.profile["Status"]

    if status == "Working":
        occupation = st.text_input("Occupation")
        income = st.slider("Monthly Income", 0, 20000, 3000)
    else:
        occupation = "Student"
        income = st.slider("Monthly Allowance", 0, 5000, 800)

    st.session_state.income = {
        "Occupation": occupation,
        "Income": income
    }

    st.caption("Income drives all ratio calculations")

    col1, col2 = st.columns(2)
    col1.button("Back", on_click=prev_step)
    col2.button("Next", on_click=next_step)
