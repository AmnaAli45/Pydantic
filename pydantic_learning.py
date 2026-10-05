from pydantic import BaseModel
from typing import List,Dict

class Patient(BaseModel):
    name:str
    age: int
    weight: float
    married: bool
    allergies : List[str]
    contact_info =Dict[str,str]
    
    
patient_info ={"name":"Amna","age":20}

patient = Patient(**patient_info)

def insert_patient_info(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")

insert_patient_info(patient)