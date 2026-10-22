import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database.database_connection import connect_db
load_dotenv()

from Model.user_model import User, get_db


app=FastAPI();
#allows computer from other origins to access the api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class RegisterUser(BaseModel):
    name:str
    email:str
    password:str
    confirmPassword:str




@app.get("/")
def get_welcome_message():
    return {"message": "Welcome to the API"}



@app.get("/api/register")
def printOk():
    return {"message": "ok"}




@app.post("/api/register")
def createnewUser(data: RegisterUser, db: Session = Depends(get_db)):
    if(len(data.password) and len(data.confirmPassword)<4 and len(data.email)==0):
        return JSONResponse(status_code=400,content={"error": "password must be atleast 4 characters"})
    if data.password != data.confirmPassword:
        return JSONResponse(status_code=400, content={"error": "Passwords do not match"})
    try:
        user = User(name=data.name, email=data.email, password=data.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"message": "User registered successfully"}
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"error": str(e)})
       
