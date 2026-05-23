# Spam Classifier (Logistic Regression from Scratch)

This project demonstrates the application of Logistic Regression to classify SMS messages into **spam** and **ham (not spam)** using a real-world dataset.

---

# Concepts Used

## Logistic Regression (From Scratch)
- Linear model: `Z = Xw + b`
- Sigmoid function for probability estimation
- Binary classification using thresholding

## Optimization
- Likelihood and log-likelihood
- Cross-entropy loss (negative log-likelihood)
- Gradient descent
- Parameter updates using gradients

## Model Evaluation
- Confusion Matrix (TP, TN, FP, FN)
- Precision
- Recall
- Accuracy

## Text Processing (NLP Basics)
- Text cleaning
- Tokenization
- Bag-of-Words representation
- Feature normalization

---

# Dataset

## SMS Spam Collection Dataset

Contains labeled SMS messages categorized as:
- Spam
- Ham (Not Spam)

Dataset Link:  
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

---

# Pipeline

Raw Text  
→ Cleaning  
→ Tokenization  
→ Vocabulary Creation  
→ Vectorization (Bag of Words)  
→ Normalization  
→ Logistic Regression  
→ Evaluation

---

# Features
- Vocabulary limited to top 1000 words to reduce overfitting
- Manual Bag-of-Words vectorization
- Logistic Regression implemented from scratch
- Training using cross-entropy loss
- Evaluation using precision, recall, and accuracy

---

# Sample Output
- Accuracy: ~85–95%
- Precision: High (low false positives)
- Recall: Moderate to high

---

# Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib

---

