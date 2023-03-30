import pandas as pd
from fastapi import FastAPI, Request, HTTPException, status, APIRouter
from sqlalchemy import create_engine
from pydantic import BaseModel


while True:
    try:
        engine = create_engine('postgresql://postgres:postgres@192.168.29.143/postgres')
        conn = engine.connect()
        print("DataBase Connected Succesfully")
        break
    except Exception as error:
        print("Error: ", error)

app = FastAPI()
router = APIRouter()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

