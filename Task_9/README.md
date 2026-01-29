# AI & ML Internship — Task 9
## Random Forest: Credit Card Fraud Detection

### Objective
The objective of this task is to build a robust fraud detection system using Random Forest and understand how ensemble models perform on highly imbalanced datasets compared to a baseline classifier.

---

### Dataset
- **Credit Card Fraud Detection Dataset**
- Source: Kaggle
- Total transactions: 284,807
- Fraud cases: Extremely rare compared to non-fraud cases
- Target variable: `Class`  
  - 0 → Non-fraud  
  - 1 → Fraud  

This dataset is highly imbalanced, making accuracy an unreliable evaluation metric.

---

### Work Performed

1. Loaded and inspected the dataset to understand feature structure and class imbalance.
2. Analyzed fraud vs non-fraud distribution to confirm severe imbalance.
3. Separated input features and target variable.
4. Split the dataset using stratified sampling to preserve fraud ratio in training and testing sets.
5. Trained a **baseline Logistic Regression model** with class balancing for comparison.
6. Trained a **Random Forest classifier** with multiple decision trees to capture non-linear patterns.
7. Evaluated models using **precision, recall, and F1-score** instead of accuracy.
8. Compared baseline and Random Forest performance to highlight improvements.
9. Visualized feature importance to identify key fraud indicators.
10. Saved the trained Random Forest model for future reuse.

---

### Model Comparison (High-Level)

- Logistic Regression acts as a baseline and prioritizes recall but produces many false positives.
- Random Forest achieves a better balance between detecting fraud and reducing false alarms.
- Ensemble learning improves performance on complex and imbalanced data.

---

### Deliverables

- Jupyter Notebook with complete workflow
- Feature importance visualization
- Saved Random Forest model file (`.pkl`)

---

### Files in This Folder

- `task9_random_forest_fraud_detection.ipynb` — Complete notebook
- `feature_importance.png` — Feature importance plot
- `random_forest_fraud_model.pkl` — Saved trained model
- `README.md` — Task overview (this file)

---

### Outcome
This task demonstrates the effectiveness of ensemble learning techniques for fraud detection and highlights best practices for handling imbalanced classification problems.
