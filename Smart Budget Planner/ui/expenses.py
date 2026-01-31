import streamlit as st
from utils.state import next_step, prev_step

def render():
    st.header("Monthly Expenses")
    st.caption(
        "Enter your average monthly spending. "
        "All values represent typical months."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.session_state.Rent = st.slider(
            "Rent",
            0,
            5000,
            st.session_state.get("Rent", 0),
            help="Monthly housing cost such as rent or mortgage. "
                 "This affects essential expense ratio."
        )

        st.session_state.Loan_Repayment = st.slider(
            "Loan Repayment",
            0,
            3000,
            st.session_state.get("Loan_Repayment", 0),
            help="Monthly payments for personal, car, or study loans."
        )

        st.session_state.Insurance = st.slider(
            "Insurance",
            0,
            2000,
            st.session_state.get("Insurance", 0),
            help="Health, vehicle, or life insurance paid monthly."
        )

    with col2:
        st.session_state.Groceries = st.slider(
            "Groceries",
            0,
            2000,
            st.session_state.get("Groceries", 0),
            help="Food and household essentials purchased for home use."
        )

        st.session_state.Transport = st.slider(
            "Transport",
            0,
            1500,
            st.session_state.get("Transport", 0),
            help="Fuel, public transport, parking, or ride services."
        )

        st.session_state.Eating_Out = st.slider(
            "Eating Out",
            0,
            1500,
            st.session_state.get("Eating_Out", 0),
            help="Restaurants, cafes, food delivery, and takeaways."
        )

    with col3:
        st.session_state.Entertainment = st.slider(
            "Entertainment",
            0,
            1500,
            st.session_state.get("Entertainment", 0),
            help="Movies, games, streaming services, and leisure spending."
        )

        st.session_state.Utilities = st.slider(
            "Utilities",
            0,
            1500,
            st.session_state.get("Utilities", 0),
            help="Electricity, water, internet, and phone bills."
        )

        st.session_state.Healthcare = st.slider(
            "Healthcare",
            0,
            1500,
            st.session_state.get("Healthcare", 0),
            help="Medical visits, medication, and health related costs."
        )

        st.session_state.Education = st.slider(
            "Education",
            0,
            2000,
            st.session_state.get("Education", 0),
            help="Tuition fees, courses, books, or learning subscriptions."
        )

        st.session_state.Miscellaneous = st.slider(
            "Miscellaneous",
            0,
            1500,
            st.session_state.get("Miscellaneous", 0),
            help="Spending not covered by other categories."
        )

    st.divider()

    nav1, nav2 = st.columns(2)

    with nav1:
        st.button("Back", on_click=prev_step)

    with nav2:
        st.button("Continue", on_click=next_step)
