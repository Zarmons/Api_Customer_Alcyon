from pydantic import BaseModel
from typing import Optional

class dataCustomerSchema(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: str

class ResponseLoginSchema(BaseModel):
    message: Optional[str]
    id: Optional[str]
    token: Optional[str]
    apiKey: Optional[str]
    clientId: Optional[str]
    status: Optional[str]

class ResponseUpdateSchema(BaseModel):
    message: Optional[str]
    id: Optional[str]
    name: Optional[str]
    email: Optional[str]
    status: Optional[str]