# Task 14 — Model Comparison & Best Model Selection

## Objective

Train and compare multiple machine learning classification models on the same dataset using identical preprocessing and train–test split. Evaluate performance using multiple metrics and select the best generalizing model.

---

## Dataset

- Dataset: Sklearn Breast Cancer Dataset
- Samples: 569
- Features: 30 numeric features
- Target: Binary classification (malignant vs benign)
- No missing values present

---

## Preprocessing

- Same train–test split used for all models (80/20, stratified).
- Feature scaling applied using **StandardScaler** for models that are scale-sensitive:
  - Logistic Regression
  - SVM
- Tree-based models used without scaling:
  - Decision Tree
  - Random Forest

This ensures fair and consistent comparison.

---

## Models Compared

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree (max_depth limited)
- Random Forest
- Support Vector Machine (RBF kernel)

Each model was trained on the same training data and evaluated on the same test set.

---

## Evaluation Metrics Used

Each model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Train Accuracy vs Test Accuracy (to detect overfitting)

All metric values were stored in a Pandas comparison table.

---

## Model Comparison Results

| Model | Train Acc | Test Acc | Precision | Recall | F1 |
|--------|------------|------------|------------|------------|------------|
Logistic Regression | 0.989 | 0.982 | 0.986 | 0.986 | **0.986**
Decision Tree | 0.993 | 0.921 | 0.957 | 0.917 | 0.936
Random Forest | 1.000 | 0.956 | 0.959 | 0.972 | 0.966
SVM | 0.982 | 0.982 | 0.986 | 0.986 | **0.986**

---

## Generalization Check

Train vs Test accuracy was compared to detect overfitting:

- Decision Tree showed higher train accuracy but lower test accuracy → signs of overfitting.
- Random Forest slightly overfit but generalized well.
- Logistic Regression and SVM showed small train–test gap → strong generalization.

---

## Best Model Selection

Best model was selected based on:

- Highest F1 score
- High test accuracy
- Low overfitting gap
- Stable generalization

**Selected Best Model: Logistic Regression**

(Logistic Regression and SVM tied on F1, Logistic Regression selected due to simpler model and strong stability.)

---

## Deliverables

- `task14_model_comparison.ipynb` — Full notebook
- `model_comparison_table.csv` — Metrics comparison table
- `model_comparison_plot.png` — Model performance bar chart
- `best_model.pkl` — Saved best model

---

## Outcome

This task demonstrates practical model comparison, overfitting detection, metric-based evaluation, and best-model selection — similar to real-world ML workflow used in industry model selection.
