from datetime import datetime
from sqlalchemy.orm import Session

from app.models.customer_model import CustomerModel
from app.schemas.customer import CustomerCreate

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


def get_customers_data(db: Session):
    return db.query(CustomerModel).all()

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