from fastapi import FastAPI, APIRouter
from router.router import customer

app = FastAPI()
app.include_router(customer)

routes_product = APIRouter()
fake_db = []