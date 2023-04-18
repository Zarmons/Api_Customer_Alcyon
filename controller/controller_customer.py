import random, string, secrets
from werkzeug.security import generate_password_hash

# Creación de llaves de acceso
def create_apikey_clienid(customer):
    apiKey = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(44)])
    clientId = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(36)])
    encryptedPassword = password_encryption(customer.password)
    data = {
        "name": customer.name,
        "email": customer.email,
        "password": encryptedPassword,
        "apiKey": apiKey,
        "clientId": clientId,
        "status": "inactive"
    }
    return data

# Encriptacion de contraseñas de usuario
def password_encryption(password):
    encryptedPassword = generate_password_hash(password, method='pbkdf2:sha256', salt_length=30)
    return encryptedPassword

# Creación de token de inicio de sesión
def generate_token():
    token = secrets.token_urlsafe(50)
    return token

# Respuesta del login
def response_login(result):
    token = generate_token()
    data = {
        "id": result.id,
        "token": token,
        "apiKey": result.apiKey,
        "clientId": result.clientId,
        "status": result.status
    }
    return data