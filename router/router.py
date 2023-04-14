from fastapi import APIRouter

customer = APIRouter()

@customer.get("/")
def root():
    return {"API´s sms directos"}