from fastapi import FastAPI
from app.routes import routes

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
