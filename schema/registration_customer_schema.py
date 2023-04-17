from pydantic import BaseModel

class RegistrationSchema(BaseModel):
    name: str
    email: str
    password: str
