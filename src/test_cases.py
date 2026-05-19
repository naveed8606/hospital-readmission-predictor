import requests

BASE_URL = "http://127.0.0.1:8000"

#testcases
test_patients = [
    {
        "name": "Low Risk Patient",
        "data": {
            "age": "[30-40)",
            "time_in_hospital": 2,
            "num_lab_procedures": 20,
            "num_procedures": 1,
            "num_medications": 5,
            "number_outpatient": 0,
            "number_emergency": 0,
            "number_inpatient": 0,
            "number_diagnoses": 3,
            "insulin": "No",
            "diabetesMed": "No",
            "change": "No"
        }
    },
    {
        "name": "Medium Risk Patient",
        "data": {
            "age": "[50-60)",
            "time_in_hospital": 5,
            "num_lab_procedures": 40,
            "num_procedures": 2,
            "num_medications": 15,
            "number_outpatient": 1,
            "number_emergency": 1,
            "number_inpatient": 1,
            "number_diagnoses": 6,
            "insulin": "Steady",
            "diabetesMed": "Yes",
            "change": "No"
        }
    },
    {
        "name": "High Risk Patient",
        "data": {
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
    }
]

print("=== API TEST RESULTS ===\n")

#test 1 - healthcheck
r = requests.get(BASE_URL + "/")
print(f"Health Check: {r.json()['status']}\n")

#test 2 - predictions + explanation
for patient in test_patients:
    r = requests.post(BASE_URL + "/predict", json=patient['data'])
    result = r.json()
    print(f"--- {patient['name']} ---")
    print(f"Risk Score : {result['risk_score']:.2%}")
    print(f"Risk Level : {result['risk_level']}")
    print(f"Explanation: {result['explanation'][:150]}...")
    print()