# ROC Curve and AUC Evaluation Report  
## Task 11 — SVM Breast Cancer Classification

---

## Objective

This report presents the ROC curve and AUC-based evaluation of the Support Vector Machine (SVM) classifier trained on the Breast Cancer dataset. The goal is to measure the model’s probability-based discrimination ability beyond simple accuracy.

---

## Dataset Summary

- Dataset: Sklearn Breast Cancer Dataset
- Total Samples: 569
- Features: 30 numerical features
- Classes:
  - Class 0 (Malignant): 212
  - Class 1 (Benign): 357

Train–Test Split:
- Training Samples: 455
- Testing Samples: 114
- Stratified split applied to preserve class distribution

---

## Model Configuration

A tuned SVM model with RBF kernel was used inside a preprocessing pipeline:

- Feature Scaling: StandardScaler
- Classifier: SVC (RBF kernel)
- Hyperparameter Tuning: GridSearchCV
- Best Parameters Found:
  - C = 10
  - gamma = 0.01
- Best Cross-Validation Score: **0.9802**

---

## Confusion Matrix (Test Set)

[[41 1]
[ 1 71]]


Interpretation:

- True Negatives: 41
- False Positives: 1
- False Negatives: 1
- True Positives: 71

Only 2 total misclassifications out of 114 test samples.

---

## Classification Performance

| Metric | Value |
|---------|---------|
Accuracy | **0.9825**
Precision (Class 1) | **0.99**
Recall (Class 1) | **0.99**
F1-Score (Class 1) | **0.99**

The classifier shows very strong precision and recall balance for the positive class.

---

## ROC Curve Analysis

The ROC (Receiver Operating Characteristic) curve was plotted using predicted class probabilities from the tuned SVM model.

ROC curve shows the trade-off between:

- True Positive Rate (Sensitivity)
- False Positive Rate

The curve stays very close to the top-left corner, indicating excellent class separation capability.

---

## AUC Score

**AUC = 0.9977**

Interpretation:

- AUC close to 1.0 indicates near-perfect discrimination ability
- The model can almost perfectly distinguish between malignant and benign cases
- Probability ranking quality is extremely high

---

## Key Findings

- Tuned RBF SVM significantly outperformed baseline linear SVM
- Hyperparameter tuning improved generalization
- Very low false positive and false negative counts
- ROC and AUC confirm strong probability calibration
- Model is highly reliable for binary classification on this dataset

---

## Conclusion

The tuned SVM classifier demonstrates excellent classification and ranking performance on the Breast Cancer dataset. With an AUC score above 0.99 and minimal misclassification, the model is highly effective for this binary classification task.

ROC and AUC evaluation confirms that the model performance is not only accurate but also robust across probability thresholds.

---
