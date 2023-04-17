import  secrets

def generate_token():
    token = secrets.token_urlsafe(50)
    return token

def response_login(token, result):
    data = {
        "message": "",
        "token": token,
        "apiKey": result.apiKey,
        "clientId": result.clientId,
        "status": result.status
    }
    return data
