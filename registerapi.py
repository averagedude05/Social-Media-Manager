import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI();
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


@app.post("/api/register")

def createnewUser(data:RegisterUser):
    if(data.password==data.confirmPassword):
        return {"message":"json received"}
    
    return JSONResponse(
        status_code=400,
        content={"error":"password doesn't match"}
        )

