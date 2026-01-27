# Model Evaluation Report  
## Decision Tree – Bank Marketing Subscription Prediction

---

## Dataset Summary

The Bank Marketing dataset contains **4,521 customer records** with demographic, financial, and campaign-related features used to predict whether a client subscribes to a term deposit.

- Total records: 4,521  
- Total features: 16  
- Target variable: `y` (subscription outcome: yes / no)

All features were either numerical or categorical, with categorical variables encoded prior to model training.

---

## Model Configuration

- **Algorithm**: Decision Tree Classifier  
- **Depth Control**: `max_depth` applied to limit overfitting  
- **Train-Test Split**: Fixed random state with stratified sampling  

Model performance was evaluated on unseen test data.

---

## Accuracy Comparison (Overfitting Check)

| Dataset | Accuracy |
|--------|----------|
| Training | 0.9090 |
| Testing  | 0.8862 |

The close gap between training and testing accuracy indicates that the model generalizes well and does not suffer from severe overfitting.

---

## Classification Performance

### Test Set Classification Report

- **Overall Accuracy**: 0.89  
- The model performs strongly for the majority (non-subscribers) class.
- Performance on the minority (subscribers) class is moderate.

| Class | Precision | Recall | F1-score | Support |
|------|----------|--------|---------|---------|
| 0 (No) | 0.92 | 0.95 | 0.94 | 801 |
| 1 (Yes) | 0.51 | 0.37 | 0.42 | 104 |

---

## Observations

- High recall for non-subscribers indicates reliable identification of customers unlikely to subscribe.
- Lower recall for subscribers reflects class imbalance and conservative positive predictions.
- Decision Tree depth limitation helped maintain stable performance across train and test sets.

---

## Conclusion

The Decision Tree model provides strong interpretability and competitive accuracy for predicting bank term deposit subscriptions.  
While overall performance is good, improving recall for the subscriber class may require class balancing techniques or ensemble methods in future iterations.

---
