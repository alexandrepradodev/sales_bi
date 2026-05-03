from fastapi import APIRouter

router = APIRouter()

@router.get("/customers")
def get_customers():
    return [
        {"customer_id": 1, "name": "Alexandre Prado"},
        {"customer_id": 2, "name": "Bruno Prado"},
        {"customer_id": 3, "name": "Gutemberg de Jesus"},
        {"customer_id": 4, "name": "Rafael Menezes"}
    ]
