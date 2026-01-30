# AI & ML Internship — Task 10
## KNN: Handwritten Digit Classification

### Objective
The objective of this task is to understand distance-based classification using the K-Nearest Neighbors (KNN) algorithm and explore how the choice of K affects model performance when classifying handwritten digits.

---

### Dataset
- **Sklearn Digits Dataset** (`load_digits()`)
- Total samples: 1,797
- Feature size: 64 (8×8 pixel images flattened)
- Target classes: Digits from 0 to 9

This dataset is preprocessed and suitable for quick experimentation with classification algorithms.

---

### Work Performed

1. Loaded the digits dataset and verified the structure of features and target labels.
2. Visualized sample digit images to confirm correct label mapping.
3. Split the dataset into training and testing sets using stratified sampling.
4. Applied feature scaling using `StandardScaler` to ensure fair distance computation.
5. Trained a KNN classifier with **K = 3** and evaluated model accuracy.
6. Experimented with multiple K values (3, 5, 7, 9) to observe performance changes.
7. Plotted **accuracy vs K** to help identify an optimal K value.
8. Generated a confusion matrix to analyze misclassified digits.
9. Displayed sample test images with predicted labels to demonstrate final output.

---

### Model Observations

- KNN achieved high accuracy on the handwritten digit dataset.
- Feature scaling significantly improved distance-based classification.
- Model performance remained stable across multiple K values.
- Lower K values provided strong accuracy while maintaining simplicity.

---

### Deliverables

- Jupyter Notebook containing complete implementation
- Accuracy vs K plot
- Confusion matrix visualization
- Sample digit prediction visualizations

---

### Files in This Folder

- `task10_knn_digits.ipynb` — Complete notebook
- `accuracy_vs_k.png` — Accuracy comparison for different K values
- `confusion_matrix.png` — Confusion matrix for KNN predictions
- `README.md` — Task overview (this file)

---

### Outcome
This task builds a clear understanding of how KNN works, why feature scaling is essential, and how tuning K impacts classification performance in image-based datasets.
