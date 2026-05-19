import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_prediction(patient_data: dict, risk_score: float, risk_level: str) -> str:
    prompt = f"""
You are a clinical decision support assistant. A machine learning model has assessed 
a diabetic patient's readmission risk.

Patient details:
- Age group: {patient_data['age']}
- Time in hospital: {patient_data['time_in_hospital']} days
- Number of medications: {patient_data['num_medications']}
- Number of lab procedures: {patient_data['num_lab_procedures']}
- Number of inpatient visits: {patient_data['number_inpatient']}
- Number of emergency visits: {patient_data['number_emergency']}
- Insulin treatment: {patient_data['insulin']}
- Diabetes medication: {patient_data['diabetesMed']}
- Medication changed: {patient_data['change']}

Prediction: {risk_level} risk of readmission within 30 days (score: {risk_score:.2%})

In 3-4 sentences explain:
1. Why this patient is {risk_level} risk
2. Which factors are most concerning
3. One specific clinical recommendation

Keep language clear for a medical professional.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )

    return response.choices[0].message.content