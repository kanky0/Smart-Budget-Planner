import streamlit as st
import pandas as pd
from ml.predict import predict_savings

REQUIRED_FIELDS = [
    "Income",
    "Age",
    "City_Tier"
]

EXPENSE_FIELDS = [
    "Rent",
    "Loan_Repayment",
    "Insurance",
    "Groceries",
    "Transport",
    "Eating_Out",
    "Entertainment",
    "Utilities",
    "Healthcare",
    "Education",
    "Miscellaneous"
]

def safe_get(key, default=0):
    return st.session_state[key] if key in st.session_state else default

def render(models, averages):
    st.header("Results")

    # -------- VALIDATION --------
    missing = []
    for field in REQUIRED_FIELDS:
        if safe_get(field, 0) in [None, "", 0]:
            missing.append(field)

    if missing:
        st.warning(
            "Missing required inputs: " + ", ".join(missing)
        )
        st.info("Please complete previous steps.")
        return

    income = safe_get("Income", 0)
    if income <= 0:
        st.warning("Income must be greater than zero.")
        return

    # -------- COLLECT INPUT --------
    raw_input = {
        "Age": safe_get("Age"),
        "Income": income,
        "Dependents": safe_get("Dependents"),
        "City_Tier": safe_get("City_Tier"),
        "Occupation": safe_get("Occupation", 0),
        "Desired_Savings": safe_get("Desired_Savings")
    }

    for col in EXPENSE_FIELDS:
        raw_input[col] = safe_get(col)

    # -------- DERIVED FEATURES --------
    total_expenses = sum(raw_input[col] for col in EXPENSE_FIELDS)

    raw_input["total_monthly_expenses"] = total_expenses
    raw_input["expense_income_ratio"] = total_expenses / income

    raw_input["dependents_income_ratio"] = (
        raw_input["Dependents"] / income
    )

    raw_input["essential_expense_ratio"] = (
        raw_input["Rent"]
        + raw_input["Groceries"]
        + raw_input["Utilities"]
        + raw_input["Healthcare"]
    ) / income

    raw_input["lifestyle_expense_ratio"] = (
        raw_input["Eating_Out"]
        + raw_input["Entertainment"]
        + raw_input["Miscellaneous"]
    ) / income

    # -------- PREDICTION --------
    try:
        savings, level = predict_savings(
            raw_input,
            models["reg"]["model"],
            models["clf"]["model"],
            models["reg"]["pipeline"],
            models["clf"]["pipeline"]
        )
    except Exception as e:
        st.error("Prediction failed.")
        st.code(str(e))
        return

    # -------- OUTPUT --------
    st.subheader("Predicted Outcome")

    st.metric(
        "Estimated Monthly Savings",
        f"${savings:,.2f}"
    )

    st.metric(
        "Savings Potential Level",
        level
    )

    # -------- CONTEXT --------
    avg = averages.get("avg_savings", None)
    if avg:
        diff = savings - avg
        st.caption(
            f"Average user saves ${avg:,.0f}. "
            f"Difference: ${diff:,.0f}"
        )

    # -------- EXPENSE VISUAL --------
    st.subheader("Expense Breakdown")

    chart_df = pd.DataFrame({
        "Category": EXPENSE_FIELDS,
        "Amount": [raw_input[c] for c in EXPENSE_FIELDS]
    })

    chart_df = chart_df[chart_df["Amount"] > 0]

    if not chart_df.empty:
        st.bar_chart(
            chart_df.set_index("Category")
        )
