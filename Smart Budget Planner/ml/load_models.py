import pickle
import json

def load_regression_pipeline():
    with open("C:\\Code\\Projects\\Smart Budget Planner\\ml\\artifacts\\pipeline_reg.pkl", "rb") as f:
        return pickle.load(f)

def load_classification_pipeline():
    with open("C:\\Code\\Projects\\Smart Budget Planner\\ml\\artifacts\\pipeline_clf.pkl", "rb") as f:
        return pickle.load(f)

def load_averages():
    with open("C:\\Code\\Projects\\Smart Budget Planner\\ml\\artifacts\\avg_stats.json", "r") as f:
        return json.load(f)
