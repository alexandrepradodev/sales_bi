from app.repositories.customer_repository import get_customers_data
from typing import Optional

def get_all_customers(
        first_name: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: str = "asc",
        page: int = 1,
        limit: int = 10
        ):
    customers = get_customers_data

    if first_name:
        customers = [
            c for c in customers
            if c["first_name"].lower() == first_name.lower()
        ]

    if sort_by:
        customers = sorted(
            customers,
            key=lambda customer: customer[sort_by],
            reverse=sort_order == "desc"
        )

    start = (page - 1) * limit
    end = start + limit

    return customers[start:end]