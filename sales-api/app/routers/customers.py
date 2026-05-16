from fastapi import APIRouter
from app.schemas.customer import Customer
from app.services.customer_service import get_all_customers
from typing import Optional

router = APIRouter()

@router.get("/customers", response_model=list[Customer])
def get_customers(
    page: int = 1,
    limit: int = 10, 
    first_name: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: str = "asc"
):
    customers = get_all_customers(first_name=first_name)

    if sort_by:
        customers = sorted(
            customers,
            key=lambda customer: customer[sort_by],
            reverse=sort_order == "desc"
        )

    if page < 1:
        page = 1

    if limit is not None:
        return customers[:limit]
    
    start = (page - 1) * limit
    end = start + limit

    return customers[start:end]