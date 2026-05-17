from fastapi import FastAPI
from app.routers import customers
from app.database.database import engine
from app.models.customer_model import CustomerModel

CustomerModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customers.router)

@app.get("/health")
def health_check():
    return {"status": "API está saudável"}