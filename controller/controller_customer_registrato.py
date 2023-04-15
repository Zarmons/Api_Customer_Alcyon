import requests, re, random, string

def create_apikey_clienid(customer):
    apiKey = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    clientId = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    data = {
        "name": customer.name,
        "email": customer.email,
        "password": customer.password,
        "apiKey": apiKey,
        "clientId": clientId,
        "status": "inactive"
    }
    return data