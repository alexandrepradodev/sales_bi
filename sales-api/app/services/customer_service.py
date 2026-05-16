from datetime import datetime
from typing import Optional

def get_all_customers(first_name: Optional[str] = None):
    customers = [
         {
            "customer_id": 1, 
            "first_name": "Alexandre",
            "last_name": "Prado",
            "email": "alexandrecarprado@gmail.com",
            "created_at": datetime.now()
            },
            {
            "customer_id": 2, 
            "first_name": "Lucas",
            "last_name": "Costa",
            "email": "lucasc2000@gmail.com",
            "created_at": datetime.now()
            }
    ]

    if first_name:
        customers = [
            c for c in customers
            if c["first_name"].lower() == first_name.lower()
        ]

    return customers