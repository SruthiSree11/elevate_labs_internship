# AI & ML Internship — Task 8
## Decision Tree: Bank Marketing Subscription Prediction

### Objective
The objective of this task is to build an interpretable classification model using a Decision Tree to predict whether a customer will subscribe to a bank term deposit based on demographic, financial, and marketing campaign data.

---

### Dataset
- **Bank Marketing Dataset**
- Source: UCI Machine Learning Repository
- Total records: 4,521
- Target variable: `y` (term deposit subscription)

---

### Work Performed

1. Loaded and inspected the Bank Marketing dataset to understand feature types and target distribution.
2. Cleaned categorical data by handling unknown or inconsistent values.
3. Encoded categorical features using One-Hot Encoding.
4. Split the dataset into training and testing sets using a fixed random state.
5. Trained a Decision Tree Classifier with controlled depth to avoid overfitting.
6. Compared training and testing accuracy to evaluate generalization.
7. Evaluated model performance using classification metrics.
8. Visualized the trained decision tree to interpret decision rules.
9. Extracted key decision rules that explain customer subscription behavior.

---

### Deliverables

- Jupyter Notebook containing full preprocessing, training, and evaluation steps
- Decision Tree visualization image
- Evaluation report with model performance metrics

---

### Files in This Folder

- `task8_decision_tree.ipynb` — Complete notebook
- `decision_tree.png` — Decision Tree visualization
- `report.md` — Model evaluation report
- `README.md` — Task overview (this file)

---

### Outcome
This task demonstrates the use of Decision Trees for interpretable machine learning and highlights how decision rules can support business-level understanding of model predictions.
