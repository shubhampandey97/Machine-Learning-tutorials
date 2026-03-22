# 📊 Feature Engineering

Feature Engineering is the process of transforming raw data into meaningful features that improve the performance of machine learning models.

This module contains **comprehensive hands-on implementations** of feature engineering techniques used in real-world machine learning pipelines.

---

# 📂 Project Structure

```text
Feature Engineering/
│
├── Feature Construction/
├── Feature Extraction/
├── Feature Transformation/
├── EncodingCategoricalData/
├── Feature Scaling/
├── missing values/
├── Outlier detection and removal/
```

---

# 🧠 Concepts & Techniques Covered

## 🔹 1. Feature Construction

Creating new features from existing data.

* Feature splitting
* Combining features
* Domain-based feature creation

---

## 🔹 2. Feature Extraction

Extracting useful information from raw data.

* Handling date & time (year, month, day, etc.)
* Handling mixed variables (numerical + categorical)

---

## 🔹 3. Encoding Categorical Data

Transforming categorical variables into numerical format.

### Techniques:

* One-Hot Encoding
* Ordinal Encoding

### Libraries Used:

* `pandas.get_dummies()`
* `sklearn.preprocessing.OneHotEncoder`
* `sklearn.preprocessing.OrdinalEncoder`

---

## 🔹 4. Feature Scaling

Scaling features to bring them to a common range.

### Techniques:

* Normalization (Min-Max Scaling)
* Standardization (Z-score scaling)
* Power Transformation (Box-Cox / Yeo-Johnson)

### Libraries Used:

* `sklearn.preprocessing.MinMaxScaler`
* `StandardScaler`
* `PowerTransformer`

---

## 🔹 5. Missing Value Handling

Handling incomplete data effectively.

### Techniques:

* Arbitrary Value Imputation
* Mean / Median Imputation
* Frequent Value (Mode) Imputation
* KNN Imputer
* Random Sample Imputation
* Missing Category Imputation
* Missing Indicator
* Complete Case Analysis
* MICE (Multiple Imputation by Chained Equations)

### Libraries Used:

* `sklearn.impute.SimpleImputer`
* `KNNImputer`
* `IterativeImputer`

---

## 🔹 6. Outlier Detection & Removal

Identifying and handling extreme values.

### Techniques:

* Percentile Method
* IQR Method
* Z-Score Method

### Libraries Used:

* `numpy`
* `scipy.stats`
* `pandas`

---

## 🔹 7. Feature Transformation

Transforming features to improve model performance.

### Techniques:

* Binning (Discretization)
* Binarization
* Function Transformer
* Power Transformation

### Libraries Used:

* `sklearn.preprocessing.FunctionTransformer`
* `KBinsDiscretizer`

---

# 🛠️ Tools & Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

# ⚙️ Workflow Followed

```text
Raw Data
   ↓
Data Cleaning
   ↓
Missing Value Handling
   ↓
Feature Encoding
   ↓
Feature Scaling
   ↓
Outlier Handling
   ↓
Feature Transformation
   ↓
Final Dataset for Model
```

---

# 🚀 How to Use

1. Navigate to any topic folder
2. Open the corresponding notebook
3. Run the notebook step-by-step
4. Understand both theory and implementation

---

# 🎯 Purpose of This Module

This module serves as:

* 📘 A complete learning resource for feature engineering
* 🧪 Hands-on implementation guide
* 💼 Portfolio project for interviews
* 🔁 Reusable reference for future ML projects

---

# 📌 Key Learnings

* How to preprocess real-world messy data
* When to use different imputation techniques
* How encoding affects model performance
* Importance of scaling and transformation
* Detecting and handling outliers effectively

---

# 👨‍💻 Author

Shubham Pandey
