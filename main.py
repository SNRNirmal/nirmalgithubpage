from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

class User(BaseModel):
    name: str
    age: int

@app.post("/create-user")
def create_user(user: User):
    return {"message": "User created", "data": user}
