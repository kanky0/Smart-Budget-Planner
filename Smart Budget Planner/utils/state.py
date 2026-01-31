import streamlit as st

DEFAULT_STATE = {
    "step": 1,

    # Profile
    "Age": 18,
    "User_Type": "Student",
    "Occupation": "",
    "City_Tier": "Tier 2",
    "Dependents": 0,

    # Income
    "Income": 0,

    # Expenses
    "Rent": 0,
    "Loan_Repayment": 0,
    "Insurance": 0,
    "Groceries": 0,
    "Transport": 0,
    "Eating_Out": 0,
    "Entertainment": 0,
    "Utilities": 0,
    "Healthcare": 0,
    "Education": 0,
    "Miscellaneous": 0,

    # Goals
    "Desired_Savings": 0
}

def init_state():
    for key, value in DEFAULT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1
