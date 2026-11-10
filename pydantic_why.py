from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int=25
    weight:float
    married: Optional[bool]=None
    allergies:list[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain= ['satiengg.in','icici.com']
        
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domain:
            raise ValueError('Not a valid Domain')
        return value
 
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    
patient_info = {'name':'Suraj','email':'suraj@saiengg.in', "weight":75.5,'allergies':['Milk','Masroom'],'contact_details':{'email':'slfee','phone':'8962856563'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
