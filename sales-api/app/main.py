from fastapi import FastAPI
from app.routers import customers

app = FastAPI()

app.include_router(customers.router)

@app.get("/health")
def health_check():
    return {"status": "API está saudável"}