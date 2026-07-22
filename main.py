# para rodar o código : uvicorn main:app --reload
from fastapi import FastAPI
app = FastAPI()

from src.routes import router

app.include_router(router)