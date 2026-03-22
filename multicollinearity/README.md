# 🔗 Multicollinearity in Machine Learning

Multicollinearity occurs when two or more independent variables in a dataset are **highly correlated**, making it difficult for models (especially linear regression) to estimate coefficients reliably.

This module provides a **practical and theoretical understanding** of multicollinearity and how to detect and handle it.

---

# 🎯 What is Multicollinearity?

Multicollinearity happens when:

* One feature can be predicted from another feature
* Features are strongly correlated

👉 This leads to unstable model coefficients.

---

# 📂 Project Structure

```text
multicollinearity/
│
├── multicollinearity.ipynb
```

---

# 🧠 Why is it a Problem?

* Coefficients become unstable
* Model interpretation becomes difficult
* Small data changes → large coefficient changes
* Increased variance in predictions

---

# 🔍 Detection Methods

## 🔹 1. Correlation Matrix

* Measures linear relationship between features
* High correlation (close to ±1) indicates multicollinearity

---

## 🔹 2. Variance Inflation Factor (VIF)

### 📌 Formula:

VIF = 1 / (1 - R²)

Where:

* R² is the coefficient of determination from regressing one feature on others

---

### 🔑 Interpretation:

* VIF = 1 → No correlation
* VIF > 5 → Moderate multicollinearity
* VIF > 10 → High multicollinearity

---

# ⚙️ Workflow

```text
Dataset
   ↓
Check Correlation Matrix
   ↓
Calculate VIF
   ↓
Identify highly correlated features
   ↓
Handle multicollinearity
```

---

# 🛠️ Handling Techniques

* Drop highly correlated features
* Use Principal Component Analysis (PCA)
* Apply Regularization (Ridge / Lasso)
* Feature selection techniques

---

# 🛠️ Tools & Libraries Used

* Python 🐍
* Pandas
* NumPy
* Seaborn (heatmap for correlation)
* Statsmodels (VIF calculation)

---

# 📊 Key Concepts

* Correlation vs Causation
* Feature redundancy
* Variance Inflation
* Model stability

---

# 🚀 Applications

* Linear Regression models
* Feature selection pipelines
* Data preprocessing workflows

---

# 📌 Key Learnings

* How to detect multicollinearity using correlation and VIF
* Why it affects regression models
* Different strategies to handle it effectively

---

# 👨‍💻 Author

Shubham Pandey
