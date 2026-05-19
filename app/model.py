import pickle
import numpy as np

PROCESSED = r'D:\Naveed\Educational\hospital-readmission-predictor\data\processed\\'

# Load model + features
with open(PROCESSED + 'model.pkl', 'rb') as f:
    model = pickle.load(f)

with open(PROCESSED + 'features.pkl', 'rb') as f:
    feature_names = pickle.load(f)

# Age mapping (same as training)
AGE_MAP = {
    '[0-10)': 0, '[10-20)': 1, '[20-30)': 2, '[30-40)': 3,
    '[40-50)': 4, '[50-60)': 5, '[60-70)': 6, '[70-80)': 7,
    '[80-90)': 8, '[90-100)': 9
}

def predict_readmission(patient_data: dict) -> dict:
    # Encode age
    patient_data['age'] = AGE_MAP.get(patient_data['age'], 5)
    
    # Encode binary fields
    patient_data['diabetesMed'] = 1 if patient_data['diabetesMed'] == 'Yes' else 0
    patient_data['change'] = 1 if patient_data['change'] == 'Ch' else 0
    
    # Encode insulin
    insulin_map = {'No': 0, 'Steady': 1, 'Up': 2, 'Down': 3}
    patient_data['insulin'] = insulin_map.get(patient_data['insulin'], 0)
    
    # Build feature array
    X = np.array([[patient_data[f] for f in feature_names]])
    
    prob = model.predict_proba(X)[0][1]
    risk_level = 'High' if prob >= 0.5 else 'Medium' if prob >= 0.3 else 'Low'
    
    return {
        'risk_score': round(float(prob), 4),
        'risk_level': risk_level
    }