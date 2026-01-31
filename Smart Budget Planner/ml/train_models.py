import pandas as pd
import numpy as np
import pickle
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from preprocessing import feature_engineering, create_pipeline

DATA_PATH = "C:/Code/Projects/Smart Budget Planner/data/data.csv"
ARTIFACT_PATH = "C:/Code/Projects/Smart Budget Planner/ml/artifacts/"

EXPENSE_COLS = [
    "Rent", "Loan_Repayment", "Insurance", "Groceries", "Transport",
    "Eating_Out", "Entertainment", "Utilities", "Healthcare",
    "Education", "Miscellaneous"
]

def compute_averages(df):
    averages = {}

    for col in EXPENSE_COLS:
        averages[col] = float(df[col].mean())

    averages["Income"] = float(df["Income"].mean())
    averages["Dependents"] = float(df["Dependents"].mean())

    return averages

df = pd.read_csv(DATA_PATH)
df = feature_engineering(df)

X_reg = df.drop(columns=["total_potential_savings"])
y_reg = df["total_potential_savings"]

X_clf = df.drop(columns=[
    "savings_potential_level",
    "total_potential_savings",
    "savings_potential_ratio"
])
y_clf = df["savings_potential_level"]

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)

pipeline_reg = create_pipeline(X_train_reg)
pipeline_clf = create_pipeline(X_train_clf)

X_train_reg_p = pipeline_reg.fit_transform(X_train_reg)
X_test_reg_p = pipeline_reg.transform(X_test_reg)

X_train_clf_p = pipeline_clf.fit_transform(X_train_clf)
X_test_clf_p = pipeline_clf.transform(X_test_clf)

rf_reg = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

rf_clf = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

rf_reg.fit(X_train_reg_p, y_train_reg)
rf_clf.fit(X_train_clf_p, y_train_clf)

y_pred_reg = rf_reg.predict(X_test_reg_p)
y_pred_clf = rf_clf.predict(X_test_clf_p)

print("Regression")
print("RMSE:", np.sqrt(mean_squared_error(y_test_reg, y_pred_reg)))
print("R2:", r2_score(y_test_reg, y_pred_reg))

print("Classification")
print("Accuracy:", accuracy_score(y_test_clf, y_pred_clf))
print("Precision:", precision_score(y_test_clf, y_pred_clf, average="weighted"))
print("Recall:", recall_score(y_test_clf, y_pred_clf, average="weighted"))
print("F1:", f1_score(y_test_clf, y_pred_clf, average="weighted"))

with open(ARTIFACT_PATH + "rf_reg.pkl", "wb") as f:
    pickle.dump(rf_reg, f)

with open(ARTIFACT_PATH + "pipeline_reg.pkl", "wb") as f:
    pickle.dump(pipeline_reg, f)

with open(ARTIFACT_PATH + "rf_clf.pkl", "wb") as f:
    pickle.dump(rf_clf, f)

with open(ARTIFACT_PATH + "pipeline_clf.pkl", "wb") as f:
    pickle.dump(pipeline_clf, f)

averages = compute_averages(df)

with open(ARTIFACT_PATH + "avg_stats.json", "w") as f:
    json.dump(averages, f, indent=2)
