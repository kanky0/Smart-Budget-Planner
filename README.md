# Title
Smart Budget Planner

# Project Overview
This project is a Streamlit based personal finance planning application. The system collects user profile, income, expenses, and goals, then produces financial summaries and model driven insights. The application focuses on clarity, guided input, and safe defaults when users complete only part of the flow.

# User Functions
- Profile setup
- Enter age, employment status, and household context.
- Student selection switches income interpretation to monthly allowance.

# Income input
- Enter salary, allowance, or other income sources.
- Helper text explains each field and expected units.

# Expense input
- Enter fixed and variable expenses.
- Helpers describe common examples such as rent, food, transport, and subscriptions.

# Goal setting
- Define savings goals and time horizon.
- Helpers explain realistic ranges and interpretation.

# Results and analysis
- View computed summaries, averages, and model outputs.
- Results remain stable even if some sections are incomplete.

# Helper System
- Each input field includes inline helper descriptions.
- Helpers explain purpose, units, and typical values.
- This mirrors the original prototype behavior.

# Usage Instructions
- Clone the repository.
- Install required Python packages.
- Run the Streamlit app.

# Open the app in a browser.
Complete sections in order.
1. Profile
2. Income
3. Expenses
4. Goals

# Navigate to Results to view outputs.
Partial completion still produces safe results.

# Input Constraints
- Numeric fields accept non negative values only.
- Monthly values use consistent currency units.
- Age must fall within a realistic human range.
- Student mode interprets income as allowance.

# Data Handling
- No user data is stored permanently.
- Sample data exists only for demonstration.
- Training data and large datasets remain excluded from version control.

# Error Handling
- Missing inputs fall back to defaults.
- Session state keys initialize before access.
- Invalid values trigger inline warnings and require correction.

# Project Structure
app.py handles application entry.
ui folder contains section specific UI files.
models folder stores trained models if present.
data folder holds optional sample data only.

# Future Enhancements
- Persistent storage support.
- Improved model explainability views.
- Additional financial scenarios and profiles.

# Author
Developed by Louis Chua Khai Yi
