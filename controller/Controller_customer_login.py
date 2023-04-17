import  secrets

def generate_token():
    token = secrets.token_urlsafe(50)
    return token

def response_login(result):
    token = generate_token()
    data = {
        "token": token,
        "apiKey": result.apiKey,
        "clientId": result.clientId,
        "status": result.status
    }
    return data
