from fastapi import APIRouter
from schema.registration_customer_schema import RegistrationSchema
from config.db import engine
from model.customers import customers
from controller.controller_customer_registrato import create_apikey_clienid

customer = APIRouter()

@customer.get("/")
def root():
    return {"API´s clientes"}

@customer.post("/post/registration")
def registration_customers(dataCustomer: RegistrationSchema):
    with engine.connect() as conn:
        verification = conn.execute(customers.select().filter(customers.c.name == dataCustomer.name).filter(customers.c.email == dataCustomer.email)).first()
    if verification:
        responseApi = "Este usuario ya existe"
    else:
        customerRegistrato = create_apikey_clienid(dataCustomer)
        with engine.connect() as conn:
            conn.execute(customers.insert().values(customerRegistrato))
            responseApi = "Usuario registrado correctamente"
        
    return responseApi
