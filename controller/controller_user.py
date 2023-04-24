import random, string, secrets
from werkzeug.security import generate_password_hash

# Creación de llaves de acceso
def create_apikey_clienid(user):
    apiKey = "".join(
        [random.choice(string.ascii_letters + string.digits) for n in range(44)]
    )
    clientId = "".join(
        [random.choice(string.ascii_letters + string.digits) for n in range(36)]
    )
    print(user)
    if user.role == None:
        role = "USER"
    else:
        role = user.role
    encryptedPassword = password_encryption(user.password)
    data = {
        "user_name": user.name,
        "user_email": user.email,
        "user_password": encryptedPassword,
        "user_apiKey": apiKey,
        "user_clientId": clientId,
        "user_status": "INACTIVE",
        "user_role": role,
    }
    return data


# Encriptacion de contraseñas de usuario
def password_encryption(password):
    encryptedPassword = generate_password_hash(
        password, method="pbkdf2:sha256", salt_length=30
    )
    return encryptedPassword


# Creación de token de inicio de sesión
def generate_token():
    token = secrets.token_urlsafe(50)
    return token


# Respuesta del login
def response_login(result):
    token = generate_token()
    data = {
        "user_id": result.user_id,
        "user_token": token,
        "user_apiKey": result.user_apiKey,
        "user_clientId": result.user_clientId,
        "user_status": result.user_status,
        "user_role": result.user_role,
    }
    return data
