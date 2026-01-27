# Model Evaluation Report  
## Logistic Regression – Titanic Survival Prediction

---

## Dataset Overview

The Titanic dataset consists of **891 passenger records** with demographic and travel-related features.  
After preprocessing and feature selection, **5 input features** were used to predict the binary target variable **Survived**.

- Total samples: 891  
- Training samples: 712  
- Testing samples: 179  
- Target variable: Survival status (0 = Not Survived, 1 = Survived)

Missing values in **Age** and **Embarked** were handled using median and mode imputation respectively.  
Categorical features were encoded, and numerical features were scaled prior to model training.

---

## Model Used

- **Algorithm**: Logistic Regression  
- **Problem Type**: Binary Classification  
- **Evaluation Data**: Test set (unseen during training)

---

## Performance Metrics

The model performance on the test dataset is summarized below:

- **Accuracy**: 0.7709  
- **Precision**: 0.7188  
- **Recall**: 0.6667  
- **F1-score**: 0.6917  
- **ROC–AUC Score**: 0.8340  

These metrics indicate that the model achieves a balanced trade-off between correctly identifying survivors and minimizing false predictions.

---

## Confusion Matrix Analysis

The confusion matrix shows:

- Strong performance in identifying non-survivors  
- Moderate false negatives, indicating some survivors were predicted as non-survivors  
- Balanced classification behavior without strong bias toward a single class  

This confirms that the model generalizes reasonably well on unseen data.

---

## ROC Curve & AUC Interpretation

The ROC curve demonstrates the relationship between the true positive rate and false positive rate across different classification thresholds.

- **AUC Score ≈ 0.83** indicates good class separability  
- The model performs significantly better than random guessing  
- ROC analysis confirms reliability beyond accuracy alone  

---

## Conclusion

The Logistic Regression model provides **stable and interpretable performance** for predicting Titanic survival outcomes.  
With proper preprocessing and evaluation, the model demonstrates strong discriminatory power as reflected by its ROC–AUC score, making it suitable as a baseline classification model for this dataset.

---
