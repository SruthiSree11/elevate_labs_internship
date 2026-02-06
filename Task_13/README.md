# Task 13 — PCA Dimensionality Reduction

## Objective
Apply Principal Component Analysis (PCA) to reduce feature dimensions of the digits dataset while preserving most of the variance. Compare model performance before and after dimensionality reduction.

---

## Dataset

- Dataset: Sklearn Digits Dataset
- Samples: 1797
- Original Features: 64 (flattened pixel values)
- Classes: 10 digit classes (0–9)
- Each sample represents an 8×8 handwritten digit image flattened into a feature vector.

---

## Steps Performed

1. Loaded digits dataset using sklearn.
2. Verified feature and label shapes.
3. Split dataset into training and testing sets using stratified sampling.
4. Applied **StandardScaler** to normalize features before PCA.
5. Trained baseline Logistic Regression model on scaled original features.
6. Applied PCA with multiple component counts (2, 10, 30, 50).
7. Recorded model accuracy for each PCA component setting.
8. Computed explained variance ratio using full PCA.
9. Plotted cumulative explained variance curve.
10. Selected number of components covering ~95% variance.
11. Transformed dataset using selected PCA components.
12. Trained Logistic Regression on reduced dataset.
13. Compared accuracy: original vs PCA-reduced features.
14. Visualized PCA 2D projection scatter plot.
15. Saved reduced dataset as CSV.

---

## Key Observations

- PCA significantly reduced feature dimensions while preserving most variance.
- Model accuracy remained comparable after dimensionality reduction.
- Around 95% variance was captured using far fewer components than original 64 features.
- PCA 2D projection showed visible class separation patterns.

---

## Deliverables

- `task13_pca.ipynb` — Full notebook
- `pca_explained_variance.png` — Cumulative variance plot
- `pca_2d_scatter.png` — PCA projection visualization
- `digits_pca_reduced.csv` — Reduced feature dataset

---

## Outcome

This task demonstrates dimensionality reduction using PCA, variance preservation analysis, and model performance comparison after feature compression.
