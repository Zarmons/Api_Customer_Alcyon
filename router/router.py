from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from config.db import engine
from werkzeug.security import check_password_hash
from schema.user_schema import dataRegistrationUserSchema, dataLoginUserSchema, ResponseLoginSchema, ResponseUpdateSchema, ResponseGetSchema
from model.users import users
from controller.controller_user import create_apikey_clienid, password_encryption, response_login

user = APIRouter()

@user.get("/")
def root():
    return {"API´s clientes"}

@user.post("/post/registration", status_code=HTTP_201_CREATED)
def registration_user(dataRegistration: dataRegistrationUserSchema):
    with engine.connect() as conn:
        verification = conn.execute(users.select().filter(users.c.user_name == dataRegistration.name).filter(users.c.user_email == dataRegistration.email)).first()
    if verification:
        responseApi = "Este usuario ya existe"
    else:
        userRegistrato = create_apikey_clienid(dataRegistration)
        with engine.connect() as conn:
            conn.execute(users.insert().values(userRegistrato))
            responseApi = Response(status_code=HTTP_201_CREATED), {"message":"Usuario creado con éxito"}
    return responseApi

@user.post("/post/login/", response_model=ResponseLoginSchema)
def login_user(dataLogin: dataLoginUserSchema ):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.user_name == dataLogin.name)).first()
        if result != None:
            check_password = check_password_hash(result[3], dataLogin.password)
            if check_password:
                message = {"message":"success"}
                responseApi = dict(response_login(result), **message)
            else:
                responseApi ={"message":"Por favor verifica tu contraseña"}
        else:
            responseApi = {"message":"Por favor verifica tu nombre de usuario"}
    return responseApi


@user.put("/update/user_password/{id}", response_model=ResponseUpdateSchema)
def update_user_password(password: str, id: str):
    with engine.connect() as conn:
        verification = conn.execute(users.select().filter(users.c.user_id == id)).first()
        if verification:
            encryptedPassword = password_encryption(password)
            result = conn.execute(users.update().values(user_password=encryptedPassword).where(users.c.user_id == id))
            if result: 
                responseApi = {"message":"contraseña cambiada con éxito"}
            else:
                responseApi = {"message":"la contraseña no se pudo cambiar"}
        else: 
            responseApi = {"message":"El usuario no existe"}
    return responseApi

@user.delete("/delete/user/{id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(id: str):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.user_id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.get("/get/users/", response_model=list[ResponseGetSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
    return result