# AI & ML Internship — Task 16  
## Hyperparameter Tuning using GridSearchCV

### Objective
The objective of this task is to improve model performance by tuning hyperparameters using GridSearchCV with cross-validation and comparing the tuned model against a default baseline model.

---

## Dataset Used
Breast Cancer Dataset from Scikit-learn

- Binary classification problem
- Features: 30 numeric measurements
- Target: Cancer class (malignant / benign)
- Loaded using sklearn.datasets.load_breast_cancer()

---

## Workflow Performed

1. Loaded the breast cancer dataset and converted it into a Pandas DataFrame.
2. Checked feature shape and class distribution.
3. Split dataset into training and testing sets using stratified sampling.
4. Built a preprocessing + model pipeline using:
   - StandardScaler for feature scaling
   - SVM classifier for modeling.
5. Trained a baseline SVM model using default hyperparameters.
6. Evaluated baseline model using:
   - Accuracy
   - Precision
   - Recall
   - F1 Score
7. Defined a hyperparameter grid for SVM including:
   - C values
   - gamma values
   - RBF kernel.
8. Applied GridSearchCV with 5-fold cross-validation to find optimal parameters.
9. Extracted best parameters and best cross-validation score.
10. Evaluated tuned model on the test dataset.
11. Created a performance comparison table between:
    - Default model
    - Tuned model.
12. Saved the best tuned pipeline model using joblib.

---

## Hyperparameter Tuning Details

Model Tuned: Support Vector Machine (SVM)

Parameters searched:
- svm__C
- svm__gamma
- svm__kernel = rbf

Method used:
- GridSearchCV
- 5-fold cross-validation
- F1-score used as tuning metric

---

## Evaluation Metrics Used

Both baseline and tuned models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

Results are shown in the notebook comparison table.

---

## Artifacts Produced

- Jupyter Notebook with full GridSearchCV workflow
- Best parameters output from GridSearchCV
- Performance comparison table
- Saved tuned model file:

tuned_svm_pipeline.pkl

---

## Outcome

Hyperparameter tuning using GridSearchCV successfully improved and validated model performance using cross-validation. The tuned SVM pipeline provides a better optimized and reusable model compared to the default configuration.
