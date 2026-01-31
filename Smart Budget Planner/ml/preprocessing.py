import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# -------------------------------
# Constants
# -------------------------------

EXPENSE_COLS = [
    "Rent", "Loan_Repayment", "Insurance", "Groceries", "Transport",
    "Eating_Out", "Entertainment", "Utilities", "Healthcare",
    "Education", "Miscellaneous"
]

# -------------------------------
# Build Features for Inference
# -------------------------------

def build_features(raw_input):
    if isinstance(raw_input, dict):
        df = pd.DataFrame([raw_input])
    else:
        df = raw_input.copy()

    # Ensure required columns exist
    required_cols = [
        "Income", "Age", "Dependents", "City_Tier", "Occupation"
    ] + EXPENSE_COLS

    for col in required_cols:
        if col not in df:
            df[col] = 0 if col not in ["City_Tier", "Occupation"] else "Unknown"

    df = feature_engineering(df)

    return df

# -------------------------------
# Feature Engineering
# -------------------------------

def feature_engineering(df):
    potential_cols = [c for c in df.columns if c.startswith("Potential_Savings_")]

    df["total_monthly_expenses"] = df[EXPENSE_COLS].sum(axis=1)
    df["expense_income_ratio"] = df["total_monthly_expenses"] / df["Income"]

    if potential_cols:
        df["total_potential_savings"] = df[potential_cols].sum(axis=1)
    else:
        df["total_potential_savings"] = 0.0

    df["savings_potential_ratio"] = df["total_potential_savings"] / df["Income"]

    df["savings_potential_level"] = df["savings_potential_ratio"].apply(
        lambda x: "Low" if x < 0.05 else "Medium" if x < 0.15 else "High"
    )

    df["savings_goal_gap"] = df["Desired_Savings"] - df["total_potential_savings"]
    df["dependents_income_ratio"] = df["Dependents"] / df["Income"]

    df["essential_expense_ratio"] = (
        df["Rent"] + df["Groceries"] + df["Utilities"] + df["Healthcare"]
    ) / df["Income"]

    df["lifestyle_expense_ratio"] = (
        df["Eating_Out"] + df["Entertainment"] + df["Miscellaneous"]
    ) / df["Income"]

    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        df[col].fillna(df[col].median(), inplace=True)

    for col in df.select_dtypes(include=["object"]).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df


# -------------------------------
# Pipeline Builder
# -------------------------------

def create_pipeline(X):
    num_cols = X.select_dtypes(include=["int64", "float64"]).columns
    cat_cols = X.select_dtypes(include=["object"]).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_cols)
        ]
    )

    return Pipeline([("preprocessor", preprocessor)])
