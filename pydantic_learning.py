from pydantic import BaseModel,field_validator
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    email: str
    age: int
    weight: float
    married: bool
    allergies : Optional[List[str]] = None
    contact_info :Dict[str,str]
    
    @field_validator('name')
    @classmethod
    def name_transformation(cls, value):
        return value.upper()
    
    @field_validator('email')
    @classmethod
    def email_validation(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value


patient_info ={"name":"Amna","age":20, "weight": 55.5, "married": False, "allergies":None, "contact_info":{"email":"amna@example.com"}}

patient = Patient(**patient_info)

def insert_patient_info(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")
    print(f"Patient Weight: {patient.weight}")
    print(f"Patient Married: {patient.married}")
    print(f"Patient Allergies: {patient.allergies}")
    print(f"Patient Contact Info: {patient.contact_info}")

insert_patient_info(patient)