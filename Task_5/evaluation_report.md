# Evaluation Report — Task 5
## Train-Test Split & Evaluation Metrics (Heart Disease Dataset)

---

## 1. Dataset Overview

- **Dataset Size:** 1025 records
- **Number of Features:** 13 input features + 1 target
- **Target Variable:** `target`
  - 1 → Presence of heart disease
  - 0 → No heart disease
- **Data Types:**
  - 13 integer features
  - 1 float feature (`oldpeak`)
- **Missing Values:** None

The dataset is fully numerical and clean, making it directly suitable for Logistic Regression without additional preprocessing.

---

## 2. Train-Test Split

- **Split Ratio:** 80% training, 20% testing
- **Test Set Size:** 205 samples
- **Stratification:** Applied on target variable to preserve class distribution

This split ensures fair evaluation and prevents data leakage while maintaining class balance.

---

## 3. Model Used

- **Algorithm:** Logistic Regression
- **Reason for Selection:**
  - Suitable for binary classification
  - Interpretable coefficients
  - Common baseline model in medical diagnosis problems

---

## 4. Evaluation Metrics Obtained

### Overall Metrics
- **Accuracy:** 0.8146
- **Precision:** 0.7638
- **Recall:** 0.9238

---

## 5. Confusion Matrix Analysis

Confusion Matrix:

[[70 30]
[ 8 97]]


| Actual \ Predicted | No Disease (0) | Disease (1) |
|-------------------|---------------|-------------|
| **No Disease (0)** | 70 (TN)       | 30 (FP)     |
| **Disease (1)**    | 8 (FN)        | 97 (TP)     |

### Interpretation:
- **True Positives (97):** Patients correctly identified as having heart disease
- **True Negatives (70):** Healthy patients correctly classified
- **False Positives (30):** Healthy patients incorrectly flagged as diseased
- **False Negatives (8):** Patients with heart disease incorrectly predicted as healthy

In healthcare, **False Negatives are the most critical errors**, as they represent missed diagnoses. This model produces **very few false negatives**, which is a strong positive outcome.

---

## 6. Classification Report Insights

-Class 0 (No Disease):

-Precision: 0.90

-Recall: 0.70

-Class 1 (Disease):

-Precision: 0.76

-Recall: 0.92


### Key Observations:
- The model achieves **high recall (0.92)** for heart disease cases, meaning it correctly identifies most patients with the condition.
- Precision for disease class (0.76) indicates some false alarms, but this trade-off is acceptable in medical screening.
- The model prioritizes **patient safety over perfect precision**, which is desirable in healthcare applications.

---

## 7. Model Behavior & Trade-offs

- The model slightly favors predicting heart disease, increasing recall.
- This leads to more false positives but significantly reduces false negatives.
- Such behavior is **appropriate for early-stage medical diagnosis**, where further medical tests can confirm predictions.

---

## 8. Conclusion

- Logistic Regression performs well as a baseline classifier for heart disease prediction.
- High recall makes the model suitable for medical screening scenarios.
- Accuracy alone does not tell the full story; confusion matrix and recall provide deeper insights.
- This task demonstrates the importance of proper evaluation beyond a single metric.


