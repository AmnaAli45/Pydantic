from pydantic import BaseModel
from typing import List,Dict

class Patient(BaseModel):
    name:str
    age: int
    weight: float
    married: bool
    allergies : List[str]
    contact_info :Dict[str,str]
    
    
patient_info ={"name":"Amna","age":20, "weight": 55.5, "married": False, "allergies":["pollen","dust"], "contact_info":{"email":"amna@example.com"}}

patient = Patient(**patient_info)

def insert_patient_info(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact Info: {patient.contact_info}")

insert_patient_info(patient)