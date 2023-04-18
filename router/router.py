from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from config.db import engine
from werkzeug.security import check_password_hash
from schema.customer_schema import dataCustomerSchema, ResponseLoginSchema, ResponseUpdateSchema
from model.customers import customers
from controller.controller_customer import create_apikey_clienid, password_encryption, response_login

customer = APIRouter()

@customer.get("/")
def root():
    return {"API´s clientes"}

@customer.post("/post/registration", status_code=HTTP_201_CREATED)
def registration_customer(dataRegistration: dataCustomerSchema):
    with engine.connect() as conn:
        verification = conn.execute(customers.select().filter(customers.c.name == dataRegistration.name).filter(customers.c.email == dataRegistration.email)).first()
    if verification:
        responseApi = "Este usuario ya existe"
    else:
        customerRegistrato = create_apikey_clienid(dataRegistration)
        with engine.connect() as conn:
            conn.execute(customers.insert().values(customerRegistrato))
            responseApi = Response(status_code=HTTP_201_CREATED), {"message":"Usuario creado con éxito"}
    return responseApi

@customer.post("/post/login/", response_model=ResponseLoginSchema)
def login_customer(dataLogin: dataCustomerSchema ):
    with engine.connect() as conn:
        result = conn.execute(customers.select().where(customers.c.name == dataLogin.name)).first()
        if result != None:
            check_password = check_password_hash(result[3], dataLogin.password)
            if check_password:
                responseApi = response_login(result)
            else:
                responseApi ={ "message":"Por favor verifica tu contraseña"}
        else:
            responseApi = {"message":"Por favor verifica tu nombre de usuario"}
    return responseApi


@customer.put("/update/customer/{id}", response_model=ResponseUpdateSchema)
def update_customer(dataUpdate: dataCustomerSchema, id: str):
    with engine.connect() as conn:
        verification = conn.execute(customers.select().filter(customers.c.id == id)).first()
        if verification:
            encryptedPassword = password_encryption(dataUpdate.password)
            conn.execute(customers.update().values(password=encryptedPassword).where(customers.c.id == id))
            result = conn.execute(customers.select().where(customers.c.id == id)).first()
            message = {"message":"usuario actualizado con éxito"}
            responseApi = dict(result, **message)
        else: 
            responseApi = {"message":"El usuario no existe"}
    return responseApi