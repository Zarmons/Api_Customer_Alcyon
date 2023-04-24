from fastapi import FastAPI, APIRouter
from router.router import user

app = FastAPI()
app.include_router(user)

routes_user = APIRouter()
fake_db = []