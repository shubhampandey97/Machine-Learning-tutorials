# 🧠 Regularization in Machine Learning

Regularization is a technique used to **reduce overfitting** by adding a penalty to the model’s complexity.

This module covers different regularization techniques including:

* Ridge Regression (L2)
* Lasso Regression (L1)
* Elastic Net
* Geometric interpretation of regularization

---

# 🎯 Why Regularization?

Machine learning models may:

* Overfit training data ❌
* Capture noise instead of pattern ❌

Regularization helps by:

* Penalizing large coefficients
* Simplifying the model
* Improving generalization

---

# 📂 Project Structure

```text
Regularization/
│
├── ridge_regression.ipynb
├── lasso-regression.ipynb
├── elastic-net-regression.ipynb
├── geometry.ipynb
```

---

# 🧠 Types of Regularization

## 🔹 1. Ridge Regression (L2 Regularization)

Adds squared penalty to coefficients.

### 📌 Formula:

J(θ) = (1/n) Σ(yᵢ - ŷᵢ)² + λ Σθⱼ²

### 🔑 Key Points:

* Shrinks coefficients
* Does NOT make them zero
* Useful when all features are important

---

## 🔹 2. Lasso Regression (L1 Regularization)

Adds absolute penalty to coefficients.

### 📌 Formula:

J(θ) = (1/n) Σ(yᵢ - ŷᵢ)² + λ Σ|θⱼ|

### 🔑 Key Points:

* Can make coefficients zero
* Performs feature selection
* Produces sparse models

---

## 🔹 3. Elastic Net

Combination of Ridge and Lasso.

### 📌 Formula:

J(θ) = (1/n) Σ(yᵢ - ŷᵢ)² + λ₁ Σ|θⱼ| + λ₂ Σθⱼ²

### 🔑 Key Points:

* Balances L1 and L2
* Useful when features are correlated

---

## 🔹 4. Geometric Interpretation

* Ridge → circular constraint
* Lasso → diamond-shaped constraint

👉 Helps understand why:

* Ridge shrinks
* Lasso selects features

---

# ⚙️ Workflow

```text
Raw Data
   ↓
Preprocessing
   ↓
Model Training (with regularization)
   ↓
Coefficient Shrinking
   ↓
Better Generalization
```

---

# 🛠️ Tools & Libraries Used

* Python 🐍
* NumPy
* Pandas
* Matplotlib
* Scikit-learn:

  * Ridge
  * Lasso
  * ElasticNet

---

# 🔧 Example (Scikit-learn)

```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=1.0)
elastic = ElasticNet(alpha=1.0, l1_ratio=0.5)
```

---

# 📊 Key Concepts

* Overfitting vs Underfitting
* Bias-Variance Tradeoff
* Regularization strength (λ)
* Coefficient shrinkage
* Feature selection

---

# 🎯 Applications

* High-dimensional datasets
* Feature selection problems
* Preventing overfitting in regression models

---

# 📌 Key Learnings

* How regularization controls model complexity
* Difference between L1 and L2 penalties
* When to use Ridge vs Lasso vs Elastic Net
* Impact of λ (regularization parameter)

---

# 👨‍💻 Author

Shubham Pandey
