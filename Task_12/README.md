# Task 12 — KMeans Customer Segmentation

## Objective
Perform customer segmentation using KMeans clustering based on customer income and spending behavior. Identify natural customer groups and interpret them as business segments.

---

## Dataset

- Dataset: Mall Customer Segmentation (Kaggle)
- Records: 200 customers
- Columns:
  - CustomerID
  - Gender
  - Age
  - Annual Income (k$)
  - Spending Score (1–100)

CustomerID was removed since it does not contribute to clustering.

---

## Features Used for Clustering

Two numerical features were selected:

- Annual Income (k$)
- Spending Score (1–100)

These features represent earning capacity and spending behavior.

---

## Steps Performed

1. Loaded dataset and inspected structure.
2. Dropped CustomerID column.
3. Selected income and spending score features.
4. Applied **StandardScaler** to normalize values (required for distance-based clustering).
5. Ran KMeans for K = 1 to 10.
6. Computed inertia values for each K.
7. Plotted **Elbow Curve** to determine optimal number of clusters.
8. Selected optimal K = 5.
9. Trained final KMeans model with K=5.
10. Added cluster labels back to dataset.
11. Visualized clusters using scatter plot.
12. Interpreted cluster centers and assigned business segment names.
13. Saved segmented dataset as CSV.

---

## Cluster Interpretation

Clusters were labeled based on average income and spending score of each cluster center:

- High Income — High Spending
- High Income — Low Spending
- Low Income — High Spending
- Low Income — Low Spending
- Average Income — Average Spending

Labels were assigned after analyzing cluster centers, not arbitrarily.

---

## Deliverables

- `task12_kmeans.ipynb` — Full notebook
- `elbow_plot.png` — Elbow method graph
- `cluster_visualization.png` — Cluster scatter plot
- `mall_customers_segmented.csv` — Dataset with cluster and segment labels

---

## Outcome

This task demonstrates unsupervised learning using KMeans clustering to segment customers into meaningful behavioral groups for business analysis and targeting.
