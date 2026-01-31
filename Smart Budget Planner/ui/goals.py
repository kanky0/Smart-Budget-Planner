import streamlit as st
from utils.state import next_step, prev_step

def render():
    st.header("Savings Goal")

    goal = st.slider("Target Monthly Savings", 0, 10000, 1000)

    st.session_state.goals = {
        "Desired_Savings": goal
    }

    st.caption("Used to measure savings gap")

    col1, col2 = st.columns(2)
    col1.button("Back", on_click=prev_step)
    col2.button("See Results", on_click=next_step)
