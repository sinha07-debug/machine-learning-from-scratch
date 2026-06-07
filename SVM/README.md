# Breast Cancer Classification using Support Vector Machine (SVM)

## Project Overview

This project uses Support Vector Machine (SVM) algorithms to classify breast tumors as **Malignant** or **Benign** using the Breast Cancer Wisconsin dataset available in Scikit-Learn.

The project explores:
- Data preprocessing
- Feature scaling
- Linear and RBF kernels
- Hyperparameter tuning
- GridSearchCV
- PCA visualization
- Decision boundary visualization
- Support vectors

---

## Dataset

The dataset was loaded using Scikit-Learn's built-in Breast Cancer Wisconsin dataset.

### Dataset Information

- Samples: 569
- Features: 30
- Classes:
  - Malignant (0)
  - Benign (1)

The features are computed from digitized images of breast mass cell nuclei.

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook

---

## Machine Learning Workflow

### 1. Data Loading

The dataset was loaded using:

```python
from sklearn.datasets import load_breast_cancer
```

### 2. Exploratory Data Analysis

Performed:
- Dataset inspection
- Missing value analysis
- Target distribution visualization
- Correlation heatmap

### 3. Data Preprocessing

- Feature and target separation
- Train-test split (80:20)
- Standardization using StandardScaler

### 4. Model Training

Two SVM models were trained:

#### Linear Kernel

```python
SVC(kernel='linear')
```

#### RBF Kernel

```python
SVC(kernel='rbf')
```

### 5. Model Evaluation

Evaluation metrics:

- Accuracy Score
- Classification Report
- Confusion Matrix

### 6. Hyperparameter Tuning

The following hyperparameters were explored:

#### Gamma

```python
gamma = [0.001, 0.01, 0.1, 1, 10, 100]
```

#### C Parameter

```python
C = [0.01, 0.1, 1, 10, 100]
```

### 7. GridSearchCV

GridSearchCV was used to automatically identify the best hyperparameter combination using 5-fold cross-validation.

### 8. PCA Visualization

Principal Component Analysis (PCA) was used to reduce the dataset from 30 dimensions to 2 dimensions for visualization.

### 9. Decision Boundary Visualization

Decision boundaries of SVM models were visualized on PCA-transformed data.

### 10. Support Vectors

Support vectors were highlighted to understand the points that influence the decision boundary.

---

## Results

| Model | Accuracy |
|---------|---------|
| Linear SVM | 95.61% |
| RBF SVM | 98.25% |

Best performance was achieved using the RBF kernel.

---

## Key Observations

- SVM achieved excellent performance on the Breast Cancer dataset.
- Feature scaling significantly improved model performance.
- The RBF kernel outperformed the linear kernel.
- Very large gamma values led to overfitting and lower test accuracy.
- Extremely small C values caused underfitting.
- GridSearchCV simplified hyperparameter optimization.
- PCA helped visualize high-dimensional data in two dimensions.
- Support vectors were the most influential points in determining the decision boundary.

---

## Project Structure

```text
svm-breast-cancer-classification/
│
├── notebooks/
│   └── svm_breast_cancer.ipynb
│
├── screenshots/
│
├── README.md
│
└── requirements.txt
```

---

## Future Improvements

- Feature selection techniques
- Comparison with Logistic Regression
- Comparison with Random Forest
- Cross-validation performance analysis
- Model deployment using Flask or Streamlit

---

## Conclusion

This project demonstrates how Support Vector Machines can be used for medical classification tasks. The RBF kernel achieved the best performance, reaching approximately 98% accuracy while successfully handling nonlinear patterns within the dataset.
