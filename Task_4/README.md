# AI & ML Internship — Task 4
## Feature Encoding & Scaling (Data-Driven Approach)

### Objective
The objective of this task is to perform feature encoding and scaling by first understanding the data distribution and then applying appropriate transformations instead of blindly scaling all numerical features.

---

## Dataset Used
- **Adult Income Dataset**
- Target variable: `income`

---

## Tools Used
- Python
- Pandas, NumPy
- Scikit-learn

---

## What Was Done

### 1. Data Understanding
- Analyzed numerical feature distributions using summary statistics and histograms.
- Checked skewness and zero-heavy features.
- Identified ordinal, nominal, and numerical features.

### 2. Feature Engineering Decisions
- **Label Encoding** applied to the binary target variable (`income`).
- **One-Hot Encoding** applied to nominal categorical features.
- **Ordinal feature (`educational-num`)** kept as-is without scaling.
- **Log transformation (`log1p`)** applied to highly skewed features (`capital-gain`, `capital-loss`).
- **StandardScaler** applied only to selected numerical features (`age`, `fnlwgt`, `hours-per-week`).
- Boolean one-hot encoded features were converted to `0/1` for model compatibility.

### 3. Final Output
- Generated a clean, fully numerical, ML-ready dataset.
- Saved the processed dataset for downstream modeling.

---

## Output Files
- `task4_feature_engineering.ipynb`
- `adult_income_preprocessed.csv`

---

## Key Learning
Feature engineering decisions should be based on data behavior and feature meaning, not only on data types. Proper encoding and scaling improve both model performance and interpretability.

---

## Conclusion
This task demonstrates a practical approach to feature encoding and scaling by combining data analysis with informed preprocessing choices, resulting in a reliable and model-ready dataset.
