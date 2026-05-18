from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from app.models.customer_model import CustomerModel
from app.schemas.customer import (CustomerCreate, CustomerUpdate)

def create_customer(db: Session, customer: CustomerCreate):

    db_customer = CustomerModel(
        first_name = customer.first_name,
        last_name = customer.last_name,
        email = customer.email
    )

    db.add(db_customer)

    db.commit()

    db.refresh(db_customer)

    return db_customer


def get_customers_data(
        db: Session,
        first_name: str = None,
        sort_by: str = None,
        sort_order: str = "asc",
        page: int = 1,
        limit: int = 10
        ):
    query = db.query(CustomerModel)

    if first_name:
        query = query.filter(
            CustomerModel.first_name.ilike(f"{first_name}")
        )

    if sort_by:
        column = getattr(CustomerModel, sort_by)

        if sort_order == "desc":
            query = query.order_by(desc(column))

        else:
            query = query.order_by(asc(column))
    
    start = (page - 1) * limit

    query = query.offset(start).limit(limit)

    return query.all()
    
def get_customer_by_id(
        db: Session,
        customer_id: int
):
    return (
        db.query(CustomerModel)
        .filter(CustomerModel.customer_id == customer_id)
        .first()
    )

def delete_customer(
        db: Session,
        customer: CustomerModel
):
    db.delete(customer)

    db.commit()

def update_customer(
        db: Session,
        customer: CustomerModel,
        customer_data: CustomerUpdate
):
    customer.first_name = customer_data.first_name
    customer.last_name = customer_data.last_name
    customer.email = customer_data.email

    db.commit()

    db.refresh(customer)

    return customer