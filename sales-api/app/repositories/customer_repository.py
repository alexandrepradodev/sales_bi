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


def get_customers_data():
    return [

        {

            "customer_id": 1,

            "first_name": "Zeca",

            "last_name": "Silva",

            "email": "zeca@email.com",

            "created_at": datetime.now()

        },

        {

            "customer_id": 2,

            "first_name": "Ana",

            "last_name": "Souza",

            "email": "ana@email.com",

            "created_at": datetime.now()

        },

        {

            "customer_id": 3,

            "first_name": "Pedro",

            "last_name": "Costa",

            "email": "pedro@email.com",

            "created_at": datetime.now()

        }

    ]