from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.customer import Customer, CustomerCreate
from app.database.database import get_db
from app.schemas.customer import CustomerCreate
from app.services.customer_service import create_new_customer, get_all_customers


router = APIRouter()

@router.get("/customers", response_model=list[Customer])
def get_customers(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),  
    first_name: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: str = "asc",
    db: Session = Depends(get_db)
):
    customers = get_all_customers(first_name=first_name, db=db)

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
        db=db,
        first_name=first_name,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        limit=limit
    )

@router.post("/customers", response_model=Customer)
def create_customer_route(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_new_customer(db=db, customer=customer)