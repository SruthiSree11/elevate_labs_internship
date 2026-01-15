# Dataset Analysis Report — Task 1

## 1. Objective
The objective of this task is to understand the structure, types, and quality of data before applying any machine learning model. Two datasets were analyzed: the Titanic dataset and the Students Performance dataset.

---

## 2. Datasets Used

### Titanic Dataset
- Rows: 891
- Columns: 12
- Type: Classification dataset
- Target Variable: Survived

### Students Performance Dataset
- Rows: 1000
- Columns: 8
- Type: Regression dataset
- Target Variables: Math score, Reading score, Writing score

---

## 3. Data Types

### Titanic Dataset
- Numerical: Age, Fare, SibSp, Parch
- Categorical: Sex, Embarked, Ticket, Cabin, Name
- Ordinal: Pclass
- Binary: Survived, Sex

### Students Dataset
- Numerical: Math score, Reading score, Writing score
- Categorical: Gender, Race/ethnicity, Parental level of education, Lunch, Test preparation course

---

## 4. Data Quality

### Titanic Dataset
- Missing values present in Age, Cabin, and Embarked columns.
- Slight class imbalance in the target variable (more non-survivors than survivors).
- Requires preprocessing like handling missing values and encoding categorical variables.

### Students Dataset
- No missing values found.
- Data is clean and well-structured.
- No class imbalance issues as it is a regression dataset.

---


## 5. ML Readiness

| Dataset   | Ready for ML? | Reason |
|--------       |---------------         |---------|
| Titanic     | Yes (after preprocessing) | Missing values and categorical encoding required |
| Students | Yes | Clean data and suitable for regression |

---

## 6. Conclusion
Both datasets are suitable for machine learning tasks. The Titanic dataset requires additional preprocessing due to missing values and categorical variables, while the Students Performance dataset is clean and directly usable for regression modeling.
