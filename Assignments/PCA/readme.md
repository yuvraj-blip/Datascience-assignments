Overview
This project explores the effects of dimensionality reduction using Principal Component Analysis (PCA) on clustering performance. We compare clustering results on the original dataset and on PCA-transformed data, analyze their differences, and provide practical recommendations for data analysis workflows.


Methodology
Data Preprocessing:

The dataset is trimmed and scaled for optimal clustering performance.

Clustering on Original Data:

K-means clustering is applied to the original dataset.

Silhouette score and visualizations are used to evaluate clustering quality.

Dimensionality Reduction with PCA:

PCA is performed to reduce the dataset to its first two principal components.

K-means clustering is then applied to this reduced dataset.

Comparison and Analysis:

Cluster quality is compared using silhouette scores and plots.

The impact of PCA on clustering is discussed.

Results
Aspect	Clustering on Original Data	Clustering after PCA
Performance (Silhouette)	0.23	0.62
Interpretability	High (original features)	Lower (principal components)
Computation	Slower	Faster
Cluster Separation	Less clear	More distinct
Clustering on original data resulted in overlapping clusters and a low silhouette score (0.23).

Clustering after PCA showed much clearer separation and a higher silhouette score (0.62).

PCA reduced noise and redundancy, improving clustering performance but making interpretation less straightforward.

Practical Implications
Use PCA before clustering when dealing with high-dimensional or highly correlated data, or when initial clustering results are poor.

Cluster on original data if interpretability of clusters (in terms of original features) is important, or if the data is already low-dimensional and well-separated.

Always evaluate clustering quality (e.g., silhouette score) and visualize results to guide your approach.

Recommendations
Apply PCA as a preprocessing step for clustering when performance is a priority over interpretability.

For explainable clustering, consider clustering on the original dataset if possible.

Use visualizations and metrics to support your analysis and decision-making.
