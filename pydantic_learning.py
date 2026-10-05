from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age: int
    
patient_info ={"name":"Amna","age":20}

patient = Patient(**patient_info)

def insert_patient_info(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patient Age: {patient.age}")

insert_patient_info(patient)