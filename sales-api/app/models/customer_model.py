from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.database import Base

class CustomerModel(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now)