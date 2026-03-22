# 📉 Gradient Descent

Gradient Descent is an optimization algorithm used to **minimize the cost function** by iteratively updating model parameters.

This module provides a **complete understanding of Gradient Descent**, including:

* Mathematical intuition
* Step-by-step implementation
* From-scratch coding
* Visual animations

---

# 🎯 What is Gradient Descent?

Gradient Descent updates model parameters (θ) in the direction of **steepest descent** of the cost function.

---

# 🧠 Core Idea

```text
Move in the direction where the cost decreases the fastest
```

---

# 📂 Project Structure

```text
Gradient Descent/
│
├── costfunction.ipynb
├── gradient-descent-step-by-step.ipynb
├── Batch-gradient-descent-from-scratch.ipynb
├── minibatch-gradient-descent-from-scratch.ipynb
├── stochastic-gradient-descent-from-scratch.ipynb
│
├── gradient-descent-animation(both-m-and-b).ipynb
├── gradient-descent-animation(onlyb).ipynb
├── Mini-Batch-Gradient-Descent-Animation.ipynb
├── stochastic-gradient-descent-animation.ipynb
```

---

# 🧮 Mathematical Formulation

## 🔹 Cost Function (MSE)

J(θ) = (1/n) Σ(yᵢ - ŷᵢ)²

---

## 🔹 Gradient Descent Update Rule

θⱼ = θⱼ - α (∂J / ∂θⱼ)

Where:

* θ → parameters (m, b)
* α → learning rate
* J(θ) → cost function

---

## 🔹 Partial Derivative

∂J / ∂θ = (2/n) Σ(yᵢ - ŷᵢ)xᵢ

---

# 🔄 Types of Gradient Descent

## 🔹 1. Batch Gradient Descent

* Uses entire dataset
* Stable but slow

---

## 🔹 2. Stochastic Gradient Descent (SGD)

* Uses one data point at a time
* Faster but noisy

---

## 🔹 3. Mini-Batch Gradient Descent

* Uses small batches
* Balance between speed and stability

---

# 🎥 Visualizations & Animations

This module includes animations for:

* Cost function contour plots
* Parameter updates (m and b)
* Convergence visualization
* SGD and Mini-batch behavior

These visualizations help understand:

* How parameters move
* How cost decreases
* Convergence patterns

---

# ⚙️ Workflow

```text
Initialize parameters (m, b)
        ↓
Compute predictions
        ↓
Calculate cost
        ↓
Compute gradients
        ↓
Update parameters
        ↓
Repeat until convergence
```

---

# 🛠️ Tools & Libraries Used

* Python 🐍
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

# 📊 Key Concepts

* Learning Rate (α)
* Convergence
* Local vs Global Minimum
* Cost Surface
* Optimization

---

# ⚠️ Important Observations

* Too high learning rate → divergence ❌
* Too low learning rate → slow convergence ❌
* Proper tuning → optimal learning ✅

---

# 🚀 Applications

* Linear Regression
* Logistic Regression
* Neural Networks
* Deep Learning optimization

---

# 📌 Key Learnings

* How optimization works in ML
* Difference between Batch, SGD, Mini-batch
* Importance of learning rate
* Visual intuition of convergence

---

# 👨‍💻 Author

Shubham Pandey
