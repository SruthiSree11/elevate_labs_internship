# AI & ML Internship — Task 5
## Train-Test Split & Evaluation Metrics

### Objective
The goal of this task is to understand how to evaluate a machine learning classification model using a proper train-test split and standard evaluation metrics.

---

### Dataset Used
- **Heart Disease Dataset**
- Binary classification problem:
  - `1` → Presence of heart disease
  - `0` → No heart disease
- The dataset contains only numerical features and has no missing values.

---

### Steps Performed

1. **Loaded the dataset**
   - Verified dataset structure, data types, and size.

2. **Identified features and target**
   - Input features: All columns except `target`
   - Target variable: `target`

3. **Performed train-test split**
   - Split the data into training and testing sets.
   - Used stratified sampling to preserve class distribution.

4. **Trained a Logistic Regression model**
   - Logistic Regression was chosen as a simple and interpretable baseline model.

5. **Made predictions on test data**
   - Predictions were generated using the trained model.

6. **Evaluated model performance**
   - Calculated accuracy, precision, and recall.
   - Used a confusion matrix to understand prediction errors.
   - Generated a classification report for detailed evaluation.

7. **Interpreted results**
   - Focused on recall due to the medical nature of the dataset.
   - Analyzed false positives and false negatives using the confusion matrix.

---

### Key Learnings
- Train-test split helps evaluate model performance on unseen data.
- Accuracy alone is not sufficient to judge a classification model.
- Confusion matrix provides deeper insight into model errors.
- Recall is especially important for medical diagnosis problems.

---

### Files in This Folder
- `task5_train_test_evaluation.ipynb` — Notebook containing all steps
- `heart.csv` — Dataset used
- `evaluation_report.md` — Detailed evaluation and interpretation
- `README.md` — Task overview (this file)

---

### Conclusion
This task provided hands-on experience in model evaluation and helped build a strong foundation in understanding how machine learning models are assessed before real-world use.
