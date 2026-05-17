from pydantic import BaseModel, EmailStr
from datetime import datetime

class Customer(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
