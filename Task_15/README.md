# AI & ML Internship — Task 15  
## End-to-End Machine Learning Pipeline

### Objective
Build a complete end-to-end Machine Learning pipeline that performs preprocessing and model training in a single integrated workflow using Scikit-learn Pipeline and ColumnTransformer.

---

## Dataset
Breast Cancer Dataset (Scikit-learn built-in dataset)

- Binary classification problem
- Predict whether tumor is malignant or benign
- All features are numeric measurements

---

## Steps Performed

1. Loaded dataset using sklearn datasets module
2. Converted data into a Pandas DataFrame
3. Separated features (X) and target (y)
4. Identified numerical and categorical feature groups
5. Built preprocessing pipeline:
   - StandardScaler applied to numerical features
6. Used ColumnTransformer to manage preprocessing
7. Built full ML pipeline combining:
   - Preprocessing stage
   - Classification model
8. Split dataset into train and test sets
9. Trained the pipeline on training data
10. Generated predictions on test data
11. Evaluated model using:
    - Accuracy
    - Precision
    - Recall
    - F1 Score
12. Saved the trained pipeline using joblib

---

## Why Pipeline Was Used

- Combines preprocessing and model into one object
- Prevents data leakage
- Ensures consistent transformations for train and test data
- Simplifies deployment and reuse

---

## Evaluation Metrics

Model performance was evaluated on test data using:

- Accuracy
- Precision
- Recall
- F1 Score

Metric values are included in the notebook output.

---

## Saved Artifacts

- Trained pipeline saved as:
  
  ml_pipeline_model.pkl

This file can be loaded later to perform predictions without repeating preprocessing steps.

---

## Outcome

A production-style ML pipeline was successfully built that integrates preprocessing and model training, demonstrating a full end-to-end machine learning workflow.
