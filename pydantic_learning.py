from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age: int
    
patient_info ={"name":"Amna","age":20}

patient = Patient(**patient_info)