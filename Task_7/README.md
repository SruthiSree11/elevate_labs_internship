# AI & ML Internship — Task 7
## Logistic Regression: Titanic Survival Prediction

### Objective
The objective of this task is to build a binary classification model using Logistic Regression to predict passenger survival on the Titanic dataset and evaluate its performance using appropriate classification metrics and visualizations.

---

### Dataset
- Titanic Dataset (loaded using Seaborn)
- Total records: 891
- Target variable: `survived`
- Selected features:
  - age
  - sex
  - fare
  - pclass
  - embarked

---

### Workflow Overview

1. Loaded and inspected the Titanic dataset to understand feature structure and missing values.
2. Handled missing values:
   - Age filled using median
   - Embarked filled using mode
3. Removed unnecessary columns not useful for prediction.
4. Encoded categorical features using One-Hot Encoding.
5. Scaled numerical features to ensure stable model training.
6. Split the dataset into training and testing sets while maintaining class distribution.
7. Trained a Logistic Regression model using a preprocessing and modeling pipeline.
8. Evaluated model performance using standard classification metrics.
9. Generated and saved performance visualizations.

---

### Evaluation Artifacts

- Confusion Matrix image
- ROC Curve with AUC score
- Classification metrics and report inside the notebook

---

### Files in This Folder

- `task7_logistic_regression.ipynb` — Complete notebook with preprocessing, modeling, and evaluation
- `confusion_matrix.png` — Confusion matrix visualization
- `roc_curve.png` — ROC curve with AUC score
- `report.md` — Model evaluation report
- `README.md` — Task overview (this file)

---

### Outcome
This task demonstrates practical understanding of binary classification, feature preprocessing, model evaluation, and performance visualization using Logistic Regression.
