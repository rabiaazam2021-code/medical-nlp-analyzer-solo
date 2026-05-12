# medical-nlp-analyzer

> Drug Review Sentiment Analysis & Named Entity Recognition System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Accuracy](https://img.shields.io/badge/Accuracy-84%25-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Overview

An end-to-end NLP pipeline that analyzes patient drug reviews to classify sentiment and extract named medical entities. Built on the UCI Drug Review Dataset with 161,297 real patient reviews.

---

## Features

- Sentiment Classification — Positive, Negative, Neutral with 84% accuracy
- Named Entity Recognition — Extracts drug names from reviews using NLTK
- Clean Prediction API — Simple functions for UI integration
- Interactive Streamlit UI — Real-time predictions

---

## Dataset

**UCI Drug Review Dataset (Drugs.com)**
- Source: UCI Machine Learning Repository (ID: 462)
- Size: 161,297 patient reviews
- License: CC BY 4.0

| Column | Type | Description |
|--------|------|-------------|
| drugName | Categorical | Name of the drug |
| condition | Categorical | Medical condition |
| review | Text | Patient review (main input) |
| rating | Numerical (1-10) | Patient satisfaction score |

### Sentiment Distribution
| Positive | Negative | Neutral |
|----------|----------|---------|
| 106,866 (66%) | 40,075 (25%) | 14,356 (9%) |

---

## Project Structure

```
medical-nlp-analyzer/
├── data/                          
├── notebooks/
│   ├── EDA.ipynb                  
│   ├── preprocessing.ipynb        
│   ├── sentiment_model.ipynb      
│   └── ner_pipeline.ipynb         
├── src/
│   └── predict.py                 
├── app/
│   └── app.py                     
├── models/                        
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Category | Tool | Purpose |
|----------|------|---------|
| Data Processing | Pandas, NumPy | Data manipulation |
| Machine Learning | Scikit-learn | TF-IDF + Logistic Regression |
| NLP / NER | NLTK | Tokenization, POS, NER |
| Visualization | Matplotlib | EDA charts |
| Web UI | Streamlit | Interactive app |

---

## Model Performance

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Positive | 0.86 | 0.96 | 0.91 |
| Negative | 0.78 | 0.77 | 0.78 |
| Neutral | 0.61 | 0.12 | 0.20 |
| **Overall Accuracy** | | | **84%** |

---

## How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/rabiaazam2021-code/medical-nlp-analyzer2.git
cd medical-nlp-analyzer2
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App
```bash
streamlit run app/app.py
```

### 4. Use Prediction API
```python
from src.predict import predict_sentiment, extract_entities

result = predict_sentiment("This drug worked great, no side effects!")
# Output: "positive"

entities = extract_entities("I took Aspirin for my headache.")
# Output: [('Aspirin', 'PERSON')]
```

---

## Team

| Name | Role | Responsibilities |
|------|------|-----------------|
| Hassan Ali | ML Engineer | EDA, Preprocessing, Sentiment Model, NER, predict.py |
| Rabia Azam | UI Engineer | Streamlit App, Integration, Deployment |

---

## License

MIT License — Dataset: CC BY 4.0