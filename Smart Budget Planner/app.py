import streamlit as st
from utils.state import init_state
from ml.load_models import (
    load_regression_pipeline,
    load_classification_pipeline,
    load_averages
)

from ui import profile, income, expenses, goals, results

st.set_page_config(page_title="Smart Budget Planner")

init_state()

models = {
    "reg": load_regression_pipeline(),
    "clf": load_classification_pipeline()
}

averages = load_averages()

step = st.session_state.step

if step == 1:
    profile.render()
elif step == 2:
    income.render()
elif step == 3:
    expenses.render()
elif step == 4:
    goals.render()
elif step == 5:
    results.render(models, averages)

# RUN: streamlit run C:\Code\Projects\Smart Budget Planner\app.py