from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status":"running"}
from database import Base, engine
from models import *

Base.metadata.create_all(bind=engine)
