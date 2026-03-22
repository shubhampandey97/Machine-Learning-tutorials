# 🔗 Scikit-Learn Pipelines

This module demonstrates how to build **end-to-end machine learning pipelines** using Scikit-learn.

Pipelines help automate preprocessing and modeling steps, ensuring consistency, reproducibility, and cleaner code.

---

# 🎯 Why Pipelines?

Without pipelines:

* Manual preprocessing ❌
* Risk of data leakage ❌
* Hard to maintain ❌

With pipelines:

* Automated workflow ✅
* No data leakage ✅
* Clean & reusable code ✅

---

# 📂 Project Structure

```text
Scikit Learn Pipelines/
│
├── predict-without-pipeline.ipynb
├── predict-using-pipeline.ipynb
├── column-transformer.ipynb
├── titanic-without-using-pipeline.ipynb
├── titanic-using-pipeline.ipynb
```

---

# 🧠 Topics Covered

## 🔹 1. Without Pipeline

* Manual preprocessing
* Separate steps for encoding, scaling, etc.
* Error-prone workflow

---

## 🔹 2. Using Pipeline

* Combining preprocessing + model
* Single object for training & prediction
* Cleaner implementation

---

## 🔹 3. Column Transformer

* Handling different column types
* Apply:

  * Scaling → numerical data
  * Encoding → categorical data

---

## 🔹 4. End-to-End Titanic Example

* Data preprocessing
* Feature engineering
* Model training
* Prediction

✔ Implemented:

* With pipeline
* Without pipeline (comparison)

---

# ⚙️ Pipeline Structure

```text
Raw Data
   ↓
Preprocessing (Imputation, Encoding, Scaling)
   ↓
Feature Transformation
   ↓
Model Training
   ↓
Prediction
```

---

# 🛠️ Tools & Libraries Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn:

  * Pipeline
  * ColumnTransformer
  * SimpleImputer
  * StandardScaler
  * OneHotEncoder

---

# 🔧 Key Components

## 🔹 Pipeline

```python
Pipeline([
    ("preprocessing", transformer),
    ("model", model)
])
```

---

## 🔹 ColumnTransformer

```python
ColumnTransformer([
    ("num", scaler, numerical_cols),
    ("cat", encoder, categorical_cols)
])
```

---

# 🚀 Advantages of Pipelines

* Prevents data leakage
* Improves reproducibility
* Simplifies deployment
* Makes code modular

---

# 🎯 Applications

* Production ML systems
* Model deployment
* Automated ML workflows

---

# 📌 Key Learnings

* Importance of structured ML workflow
* Combining preprocessing and model
* Handling mixed data types efficiently

---

# 👨‍💻 Author

Shubham Pandey
