from pydantic import BaseModel
from typing import Optional

class RegistrationSchema(BaseModel):
    name: str
    email: str
    password: str

class ResponseCustomerSchema(BaseModel):
    message: str