from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.customer import Customer, CustomerCreate
from app.database.database import get_db
from app.schemas.customer import (CustomerCreate, CustomerUpdate)
from app.services.customer_service import create_new_customer, get_all_customers
from app.services.customer_service import (get_customer, remove_customer, update_existing_customer)


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

@router.get("/customers/{customer_id}", response_model=Customer)
def get_customer_by_id_route(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = get_customer(
        db=db,
        customer_id=customer_id
    )
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )
    return customer

@router.post("/customers", response_model=Customer)
def create_customer_route(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_new_customer(db=db, customer=customer)

@router.delete("/customers/{customer_id}", status_code=204)
def delete_customer_route(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = remove_customer(
        db=db,
        customer_id=customer_id
    )
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado na base de dados"
        )
    
@router.put("/customers/{customer_id}", response_model=Customer)
def update_customer_route(
    customer_id: int,
    customer_data: CustomerUpdate,
    db: Session = Depends(get_db)
):
    customer = update_existing_customer(
        db=db,
        customer_id=customer_id,
        customer_data=customer_data
    )
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado na base de dados"
        )
    return customer