from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import predict_readmission
from app.agent import explain_prediction
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Hospital Readmission Predictor",
    description="Predicts 30-day readmission risk for diabetic patients using ML + AI explanation",
    version="1.0.0"
)

class PatientInput(BaseModel):
    age: str
    time_in_hospital: int
    num_lab_procedures: int
    num_procedures: int
    num_medications: int
    number_outpatient: int
    number_emergency: int
    number_inpatient: int
    number_diagnoses: int
    insulin: str
    diabetesMed: str
    change: str

class PredictionOutput(BaseModel):
    risk_score: float
    risk_level: str
    explanation: str

@app.get("/")
def root():
    return {"message": "Hospital Readmission Predictor API", "status": "running"}

@app.post("/predict", response_model=PredictionOutput)
def predict(patient: PatientInput):
    try:
        # Predict
        patient_dict = patient.dict()
        result = predict_readmission(patient_dict.copy())
        
        # AI explanation
        explanation = explain_prediction(
            patient_dict,
            result['risk_score'],
            result['risk_level']
        )
        
        return {
            'risk_score': result['risk_score'],
            'risk_level': result['risk_level'],
            'explanation': explanation
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))