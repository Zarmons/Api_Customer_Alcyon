from pydantic import BaseModel
from typing import Optional

class LoginSchema(BaseModel):
    name: str
    password: str

class ResponseLoginSchema(BaseModel):
    message: str
    token: Optional[str]
    apiKey: Optional[str]
    clientId: Optional[str]
    status: Optional[str]