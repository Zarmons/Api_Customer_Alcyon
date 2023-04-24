from pydantic import BaseModel
from typing import Optional

class dataRegistrationUserSchema(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str]

class dataLoginUserSchema(BaseModel):
    name: str
    password: str

class ResponseLoginSchema(BaseModel):
    message: Optional[str]
    user_id: Optional[str]
    user_token: Optional[str]
    user_apiKey: Optional[str]
    user_clientId: Optional[str]
    user_status: Optional[str]
    user_role: Optional[str]

class ResponseUpdateSchema(BaseModel):
    message: str


class ResponseGetSchema(BaseModel):
    user_id: str
    user_name: str
    user_email: str
    user_password:str
    user_apiKey: str
    user_clientId: str
    user_status: str
    user_role: str