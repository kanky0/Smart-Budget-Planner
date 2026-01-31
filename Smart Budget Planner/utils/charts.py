import pandas as pd
import streamlit as st

def category_comparison(user_vals, avg_vals):
    df = pd.DataFrame({
        "You": user_vals,
        "Average": avg_vals
    }, index=["Essential", "Lifestyle"])

    st.bar_chart(df)

def savings_simulation(base_savings):
    scenarios = {
        "Current": base_savings,
        "10% Cut": base_savings * 1.1,
        "20% Cut": base_savings * 1.2,
        "30% Cut": base_savings * 1.3
    }

    st.line_chart(scenarios)
