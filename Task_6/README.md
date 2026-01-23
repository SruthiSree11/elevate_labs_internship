# AI & ML Internship — Task 6
## Linear Regression: House Price Prediction

### Objective
The objective of this task is to build a complete regression pipeline using Linear Regression and understand how to evaluate prediction performance using appropriate error metrics.

---

### Dataset Used
- **California Housing Dataset**
- Loaded directly using `sklearn.datasets`
- Contains numerical features related to housing characteristics and location
- Target variable represents median house value

---

### Work Done in This Task

1. **Dataset Loading**
   - Loaded the California housing dataset.
   - Converted it into a Pandas DataFrame for better visibility of features and target.

2. **Data Inspection**
   - Examined dataset structure, data types, and value ranges using basic inspection methods.
   - Confirmed that the target variable is continuous, making it a regression problem.

3. **Feature and Target Separation**
   - Separated input features (`X`) and target variable (`y`).

4. **Train-Test Split**
   - Split the dataset into training and testing sets using a fixed random state.
   - Ensured the model is evaluated on unseen data.

5. **Model Training**
   - Trained a Linear Regression model using the training dataset.

6. **Prediction**
   - Generated predictions on the test dataset.
   - Created a comparison table of actual vs predicted house prices.

7. **Model Evaluation**
   - Evaluated the model using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
   - Used these metrics to understand prediction error magnitude.

8. **Visualization**
   - Plotted predicted values against actual values to visually assess model performance.

9. **Model Interpretation**
   - Analyzed model coefficients to identify features that most strongly influence house prices.

---

### Files in This Folder
- `task6_linear_regression.ipynb` — Jupyter notebook containing the complete workflow
- `report.md` — Evaluation report with MAE and RMSE results
- `README.md` — Task overview (this file)

---

### Conclusion
This task demonstrates a complete regression workflow, from data loading and model training to evaluation and interpretation, providing a strong foundation in linear regression modeling.
