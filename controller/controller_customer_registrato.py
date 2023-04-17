import random, string
from werkzeug.security import generate_password_hash

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

def password_encryption(password):
    encryptedPassword = generate_password_hash(password, method='pbkdf2:sha256', salt_length=30)
    return encryptedPassword