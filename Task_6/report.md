# Model Evaluation Report — Task 6
## Linear Regression: House Price Prediction

---

## Dataset
- California Housing Dataset
- Test Set Size: 4,128 samples

---

## Evaluation Metrics

The Linear Regression model was evaluated on the test dataset using standard regression error metrics.

- **Mean Absolute Error (MAE):** 0.5332  
- **Root Mean Squared Error (RMSE):** 0.7456  

---

## Interpretation of Results

- The MAE value indicates that, on average, the model’s predicted house prices differ from the actual values by approximately 0.53 units.
- The RMSE value is higher than MAE, showing that some predictions have larger errors, which is expected in real-world house price prediction.
- The difference between MAE and RMSE suggests the presence of higher-error cases, especially for houses with extreme prices.

---

## Performance Summary

- The model provides reasonable baseline performance for house price prediction.
- Errors are acceptable for a simple Linear Regression model.
- Results indicate potential underfitting, suggesting that more complex models may further improve prediction accuracy.

---

## Conclusion

The MAE and RMSE values demonstrate that Linear Regression can capture general trends in house prices but has limitations in handling complex, non-linear relationships present in the dataset.
