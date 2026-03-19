# AI Support Chatbot

This project is an NLP-based chatbot built with Python.

Features:
- Text classification
- Real-world dataset usage
- Machine learning models

Currently improving:
- LLM integration
- RAG (Retrieval-Augmented Generation)
- API development with FastAPI

---

<h1 align="center">🧠 NLP Support Ticket Classification System</h1>

<p align="center">
AI-based system for classifying and prioritizing customer support messages
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/NLP-Project-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Ongoing-yellow?style=for-the-badge"/>
</p>

---

🚀 This project simulates a real-world AI customer support automation system used in modern applications.

## 📌 Overview

This project focuses on building an AI-powered system that automatically analyzes and classifies customer support messages into relevant categories.

---

## ⚡ Features

* Text classification (Complaint, Payment, Account, Delivery)
* Priority prediction (Low / Medium / High)
* Semantic similarity (Cosine Similarity)
* Automated response suggestions

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* TF-IDF
* (Planned: BERT)
* 📦 Dependencies listed in requirements.txt

---

## 🚀 How it works

1. Text preprocessing
2. Feature extraction using TF-IDF
3. Model training (Logistic Regression)
4. Prediction

---

## 📊 Example

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = ["Siparişim gelmedi", "Ödeme yaptım ama görünmüyor"]
labels = ["delivery", "payment"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

test = ["Siparişim çok geç geldi"]
X_test = vectorizer.transform(test)

print(model.predict(X_test))
