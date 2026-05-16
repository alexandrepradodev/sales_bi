from fastapi import APIRouter, HTTPException, Query
from app.schemas.customer import Customer
from app.services.customer_service import get_all_customers
from typing import Optional

router = APIRouter()

@router.get("/customers", response_model=list[Customer])
def get_customers(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),  
    first_name: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: str = "asc"
):
    customers = get_all_customers(first_name=first_name)

    allowed_sort_fields = [
        "first_name",
        "last_name",
        "email",
        "created_at"
    ]

    allowed_sort_orders = [
        "asc",
        "desc"
    ]

    if sort_by and sort_by not in allowed_sort_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field: {sort_by}"
        )
    
    if sort_order not in allowed_sort_orders:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort order: {sort_order}"
        )
    
    return get_all_customers(
        first_name=first_name,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        limit=limit
    )