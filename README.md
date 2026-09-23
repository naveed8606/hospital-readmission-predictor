# Hospital Readmission Risk Predictor

[![Live API](https://img.shields.io/badge/API-Live-brightgreen)](https://hospital-readmission-predictor-2-qkmw.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-teal)](https://fastapi.tiangolo.com)
[![Groq](https://img.shields.io/badge/AI-Groq%20LLaMA-orange)](https://groq.com)

## What this does

Diabetes is the leading cause of preventable hospital readmissions globally. When a patient is discharged without identifying their readmission risk, hospitals lose the window to intervene — and patients pay the price.

This project builds a REST API that takes a diabetic patient's clinical data, predicts their probability of being readmitted within 30 days, and generates a plain-English clinical explanation using an LLM agent. The goal is to give clinicians a fast, actionable signal at the point of discharge — not a black-box score they can't use.

**Live API:** https://hospital-readmission-predictor-2-qkmw.onrender.com/docs

---

## Why it's built this way

Most ML projects stop at a Jupyter notebook. This one goes further:

- The model is served via **FastAPI** — meaning any frontend, mobile app, or hospital system can call it over HTTP
- Predictions are explained in **plain clinical language** via a Groq LLaMA agent — because a risk score alone isn't actionable
- The whole thing is **deployed on Render** — not just running locally

The stack mirrors how production ML systems actually work.

---

## How it works

```
Clinical data (JSON) → FastAPI → Gradient Boosting model → Risk score
                                                                ↓
                                              Groq LLaMA agent explains why
                                                                ↓
                                              JSON response with score + explanation
```

---

## Use Cases

- **At discharge** — flag high-risk patients before they leave the ward, giving clinicians a window to intervene
- **Care coordination** — prioritise follow-up calls and home visits for patients with high predicted risk
- **Resource planning** — identify which patient profiles and departments drive the most readmissions
- **Clinical decision support** — give junior doctors an evidence-based second opinion on discharge decisions
- **Research** — benchmark ML approaches against traditional readmission scoring tools like LACE or HOSPITAL score

---

## API

| Method | Endpoint | What it does |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/predict` | Returns risk score, level, and AI explanation |
| GET | `/docs` | Swagger UI — test it in the browser |

**Request:**
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

**Response:**
```json
{
  "risk_score": 0.73,
  "risk_level": "High",
  "explanation": "This patient presents several high-risk indicators: 
  4 prior inpatient admissions, 3 emergency visits, and an escalating 
  insulin regimen suggest poorly controlled diabetes. A structured 
  discharge plan with follow-up within 48 hours is strongly recommended."
}
```

---

## Model Performance

Three classifiers were trained and compared on the UCI Diabetes dataset (100,000 records):

| Model | AUC |
|-------|-----|
| Logistic Regression | 0.6133 |
| Random Forest | 0.5732 |
| **Gradient Boosting** | **0.6210** ✅ |

Gradient Boosting was selected for deployment. AUC of 0.62 is consistent with published benchmarks on this dataset given class imbalance (~11% positive class).

---

## Dataset

UCI Diabetes 130-US Hospitals (1999–2008)
- 100,000 inpatient records across 130 US hospitals
- Features: demographics, diagnoses, lab results, medications, prior visits
- Target: readmitted within 30 days (binary)
- [Source](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)

---

## Project Structure

```
hospital-readmission-predictor/
├── app/
│   ├── main.py          ← FastAPI routes
│   ├── model.py         ← Model loading + inference
│   └── agent.py         ← LLM explanation agent
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_model.ipynb
├── src/
│   └── test_cases.py
├── reports/
├── data/
│   ├── raw/
│   └── processed/
├── render.yaml
└── requirements.txt
```

---

## Run Locally

```bash
git clone https://github.com/naveed8606/hospital-readmission-predictor.git
cd hospital-readmission-predictor
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:
```
GROQ_API_KEY=your_key_here
```

Get a free Groq key at [console.groq.com](https://console.groq.com)

Download dataset → place `diabetic_data.csv` in `data/raw/` → run notebooks in order → then:

```bash
uvicorn app.main:app --reload
# Open http://127.0.0.1:8000/docs
```

---

## Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| API Framework | FastAPI + Uvicorn |
| ML Model | Scikit-learn (Gradient Boosting) |
| AI Agent | Groq LLaMA |
| Data Processing | Pandas + NumPy |
| Notebooks | Jupyter |
| Deployment | Render |

---

**Naveed Nihan** · [GitHub](https://github.com/naveed8606)