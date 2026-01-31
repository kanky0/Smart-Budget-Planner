# Title
Smart Budget Planner

# Overview
Smart Budget Planner is an AI driven personal finance web application that predicts monthly savings potential and classifies savings behavior.

The system uses supervised machine learning models trained on demographic and expense data. A Streamlit interface guides users through a structured onboarding flow, collects financial inputs with explanations, and presents predictions with visual feedback.

This project is designed to be practical, interpretable, and extensible. It is suitable for academic work, portfolio demonstration, or as a foundation for a real money tracking application.

# Features
• Multi step guided onboarding flow
• Conditional inputs for students and working users
• Contextual helpers explaining each financial field
• Robust handling of partial or missing inputs
• Monthly savings amount prediction
• Savings potential level classification
• Expense breakdown visualizations
• Feature engineered financial ratios
• Clean separation between ML and UI code
• Models persisted and reused consistently

# Machine Learning Approach
Regression Task
Predicts estimated monthly savings potential.

Classification Task
Predicts savings behavior level. Low, Medium, or High.

# Models
• Random Forest Regressor
• Random Forest Classifier

Why Random Forest
• Strong performance on tabular data

• Handles non linear relationships

• Resistant to overfitting

• Feature importance available for explainability

Feature Engineering
• Total monthly expenses
• Expense to income ratio
• Essential expense ratio
• Lifestyle expense ratio
• Dependents to income ratio
• Savings goal gap

Data Leakage Prevention
• Classification target derived after feature construction
• Leakage features removed from classification inputs
• Separate pipelines for regression and classification
