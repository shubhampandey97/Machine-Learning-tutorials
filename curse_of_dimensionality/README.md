# 📉 Curse of Dimensionality & Dimensionality Reduction

This module focuses on understanding the **Curse of Dimensionality** and applying **Principal Component Analysis (PCA)** to reduce feature space while preserving important information.

It includes both **theoretical understanding** and **hands-on implementation** using real datasets.

---

# 🧠 What is Curse of Dimensionality?

As the number of features (dimensions) increases:

* Data becomes sparse
* Distance between points becomes less meaningful
* Model performance degrades
* Computational cost increases

This phenomenon is known as the **Curse of Dimensionality**.

---

# 🎯 Why Dimensionality Reduction?

Dimensionality reduction helps to:

* Improve model performance
* Reduce overfitting
* Decrease training time
* Remove noise and redundant features
* Enable visualization of high-dimensional data

---

# 📂 Project Structure

```text
curse_of_dimensionality/PCA/
│
├── pca_step_by_step.ipynb
├── pca_task.ipynb
├── PCA_mnist.ipynb
├── visalisation.ipynb
```

---

# 🔬 Topics Covered

## 🔹 1. Understanding PCA

* Variance and covariance
* Eigenvalues and eigenvectors
* Projection of data onto principal components

---

## 🔹 2. PCA Step-by-Step Implementation

* Standardization of data
* Covariance matrix calculation
* Eigen decomposition
* Selecting top components
* Transforming dataset

---

## 🔹 3. PCA on Real Dataset (MNIST)

* High-dimensional image data
* Dimensionality reduction using PCA
* Performance improvement analysis

---

## 🔹 4. Visualization of High-Dimensional Data

* Reducing data to 2D/3D
* Visualizing clusters
* Understanding separability

---

# 🛠️ Tools & Libraries Used

* Python 🐍
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn (`sklearn.decomposition.PCA`)
* Jupyter Notebook

---

# ⚙️ Workflow

```text
High-Dimensional Data
        ↓
Data Standardization
        ↓
Covariance Matrix
        ↓
Eigen Decomposition
        ↓
Select Top Components
        ↓
Transform Data
        ↓
Visualization / Model Training
```

---

# 📊 Key Concepts

* Variance maximization
* Orthogonal components
* Explained variance ratio
* Dimensionality reduction trade-offs

---

# 🚀 How to Use

1. Start with `pca_step_by_step.ipynb` for understanding
2. Move to `pca_task.ipynb` for practice
3. Explore `PCA_mnist.ipynb` for real-world application
4. Use `visalisation.ipynb` to understand data representation

---

# 🎯 Applications

* Image compression
* Noise reduction
* Feature extraction
* Data visualization
* Preprocessing before ML models

---

# 📌 Key Learnings

* Why high dimensions hurt model performance
* How PCA reduces dimensions effectively
* Importance of variance in feature selection
* Trade-off between information loss and simplicity

---

# 👨‍💻 Author

Shubham Pandey
