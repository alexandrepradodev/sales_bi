from pydantic import BaseModel, EmailStr
from datetime import datetime

class Customer(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    email: EmailStr
    created_at: datetime