import requests

patient = {
    "age": "[50-60)",
    "time_in_hospital": 5,
    "num_lab_procedures": 40,
    "num_procedures": 2,
    "num_medications": 15,
    "number_outpatient": 0,
    "number_emergency": 1,
    "number_inpatient": 2,
    "number_diagnoses": 7,
    "insulin": "Steady",
    "diabetesMed": "Yes",
    "change": "Ch"
}

response = requests.post("http://127.0.0.1:8000/predict", json=patient)
result = response.json()

print("=== PREDICTION RESULT ===")
print(f"Risk Score: {result['risk_score']}")
print(f"Risk Level: {result['risk_level']}")
print(f"\nAI Explanation:\n{result['explanation']}")