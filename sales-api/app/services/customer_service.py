from typing import Optional
from sqlalchemy.orm import Session

from app.repositories.customer_repository import get_customers_data
from app.schemas.customer import CustomerCreate
from app.repositories.customer_repository import create_customer

def create_new_customer(
        db: Session,
        customer: CustomerCreate
):
    return create_customer(db, customer)


def get_all_customers(
        db: Session,
        first_name: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: str = "asc",
        page: int = 1,
        limit: int = 10
        ):
    customers = get_customers_data(db)

    if first_name:
        customers = [
            customer for customer in customers
            if customer.fist_name.lower() == first_name.lower()
        ]

    if sort_by:
        customers = sorted(
            customers,
            key=lambda customer: getattr(customer, sort_by),
            reverse=sort_order == "desc"
        )

    start = (page - 1) * limit
    end = start + limit

    return customers[start:end]