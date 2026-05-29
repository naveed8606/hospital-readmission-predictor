# Hospital Readmission Risk Predictor

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![AI](https://img.shields.io/badge/AI-Groq%20LLaMA-orange)

## Overview
An end-to-end ML system that predicts 30-day hospital readmission risk for diabetic patients. Combines a Gradient Boosting classifier with a Groq LLaMA AI agent that explains predictions in plain clinical language via a FastAPI REST API.

## Live Demo
```bash
uvicorn app.main:app --reload
python src/test_cases.py
```

## Research Question
> *"Can clinical patient data predict 30-day readmission risk for diabetic patients, and can AI explain these predictions in actionable clinical language?"*

## Results
| Model | AUC Score |
|-------|-----------|
| Logistic Regression | 0.6133 |
| Random Forest | 0.5732 |
| **Gradient Boosting** | **0.6210** |

## Architecture

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/predict` | Predict readmission risk |
| GET | `/docs` | Interactive API docs |

## Sample Request
```json
{
  "age": "[70-80)",
  "time_in_hospital": 10,
  "num_lab_procedures": 65,
  "num_procedures": 4,
  "num_medications": 22,
  "number_outpatient": 2,
  "number_emergency": 3,
  "number_inpatient": 4,
  "number_diagnoses": 9,
  "insulin": "Up",
  "diabetesMed": "Yes",
  "change": "Ch"
}
```

## Sample Response
```json
{
  "risk_score": 0.73,
  "risk_level": "High",
  "explanation": "This patient is high risk due to multiple prior inpatient visits, elevated emergency admissions, and increasing insulin dosage..."
}
```

## Project Structure
```
hospital-readmission-predictor/
├── app/
│   ├── main.py          ← FastAPI endpoints
│   ├── model.py         ← ML model + prediction
│   └── agent.py         ← Groq AI explanation
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_model.ipynb
├── src/
│   └── test_cases.py    ← API tests
├── reports/             ← Charts + visualisations
├── data/
│   ├── raw/             ← Original dataset
│   └── processed/       ← Model + features
├── .env                 ← API keys (not committed)
└── requirements.txt
```


## Dataset
UCI Diabetes 130-US Hospitals Dataset — 100,000 patient records (1999-2008)
[UCI ML Repository](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)

## Tech Stack
Python · FastAPI · Scikit-learn · Groq LLaMA · Pandas · Uvicorn · Jupyter

## How to Run

### 1. Clone repo
```bash
git clone https://github.com/naveed8606/hospital-readmission-predictor.git
cd hospital-readmission-predictor
```

### 2. Setup environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add API key

GROQ_API_KEY=your_groq_key_here

### 4. Download dataset
Place `diabetic_data.csv` in `data/raw/` → run notebooks in order

### 5. Start API
```bash
uvicorn app.main:app --reload
```

### 6. Test
```bash
python src/test_cases.py
```

## Author
**Naveed Nihan**