# Task 11 — SVM Breast Cancer Classification

## Objective
Build a Support Vector Machine (SVM) classifier to predict whether a tumor is malignant or benign using the Breast Cancer dataset. Compare linear and RBF kernels, tune hyperparameters, and evaluate using ROC and AUC metrics.

---

## Dataset

- Source: Scikit-learn built-in Breast Cancer dataset
- Samples: 569
- Features: 30 numeric features
- Target Classes:
  - 0 → Malignant
  - 1 → Benign

No missing values present.

---

## Steps Performed

1. Loaded dataset using `load_breast_cancer()`.
2. Checked dataset shape and class distribution.
3. Split data into train and test sets using stratified sampling.
4. Applied **StandardScaler** because SVM is scale-sensitive.
5. Built pipeline (Scaler + SVM).
6. Trained baseline SVM with **Linear kernel**.
7. Trained SVM with **RBF kernel** and compared performance.
8. Tuned hyperparameters using **GridSearchCV** (C and gamma).
9. Evaluated tuned model using:
   - Accuracy
   - Classification report
   - Confusion matrix
10. Plotted ROC curve and computed AUC score.
11. Saved final tuned pipeline model using `joblib`.

---

## Model Results (Best Tuned SVM)

- Kernel: RBF
- Best Parameters:
  - C = 10
  - gamma = 0.01

### Test Performance
- Accuracy: 0.982
- Very low misclassification
- Strong precision and recall balance

### ROC–AUC
- AUC Score ≈ 0.998
- Indicates near-perfect class discrimination

---

## Files Included

- `task11_svm_breast_cancer.ipynb` — Full notebook
- `svm_roc_curve.png` — ROC curve plot
- `svm_breast_cancer_pipeline.pkl` — Saved trained model
- `roc_auc_report.md` — Detailed ROC & AUC evaluation report

---

## Outcome

This task demonstrates kernel-based classification, feature scaling importance, hyperparameter tuning, and probability-based model evaluation using ROC and AUC.
