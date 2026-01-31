from .preprocessing import build_features

def predict_savings(raw_input, reg_model, clf_model, reg_pipeline, clf_pipeline):
    X_raw = build_features(raw_input)

    X_reg = reg_pipeline.transform(X_raw)
    X_clf = clf_pipeline.transform(X_raw)

    savings_amount = reg_model.predict(X_reg)[0]
    savings_level = clf_model.predict(X_clf)[0]

    return savings_amount, savings_level
