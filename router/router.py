from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from config.db import engine
from werkzeug.security import check_password_hash

from schema.registration_customer_schema import RegistrationSchema
from schema.login_customer_schema import LoginSchema, ResponseLoginSchema
from model.customers import customers
from controller.controller_customer_registrato import create_apikey_clienid
from controller.Controller_customer_login import generate_token, response_login

customer = APIRouter()

@customer.get("/")
def root():
    return {"API´s clientes"}

@customer.post("/post/registration", status_code=HTTP_201_CREATED)
def registration_customers(dataCustomer: RegistrationSchema):
    with engine.connect() as conn:
        verification = conn.execute(customers.select().filter(customers.c.name == dataCustomer.name).filter(customers.c.email == dataCustomer.email)).first()
    if verification:
        responseApi = "Este usuario ya existe"
    else:
        customerRegistrato = create_apikey_clienid(dataCustomer)
        with engine.connect() as conn:
            conn.execute(customers.insert().values(customerRegistrato))
            responseApi = Response(status_code=HTTP_201_CREATED), "usuario creado con éxito"
    return responseApi

@customer.post("/post/login/", response_model=ResponseLoginSchema)
def login_customer(dataLoginClient: LoginSchema ):
    with engine.connect() as conn:
        result = conn.execute(customers.select().where(customers.c.name == dataLoginClient.name)).first()
        print(result)
        if result != None:
            check_password = check_password_hash(result[3], dataLoginClient.password)
            if check_password:
                token = generate_token()
                responseApis = response_login(token, result)
            else:
                responseApis ={ "message":"Por favor verifica tu contraseña"}
        else:
            responseApis = {"message":"Por favor verifica tu nombre de usuario"}
    return responseApis
