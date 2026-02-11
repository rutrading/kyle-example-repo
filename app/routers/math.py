from fastapi import APIRouter, HTTPException

from app.schemas.math import AddRequest, MathResult

router = APIRouter(prefix="/math", tags=["math"])


@router.get("/add/{a}/{b}", response_model=MathResult)
def add_numbers(a: int, b: int):
    return MathResult(result=a + b)


@router.post("/add", response_model=MathResult)
def add_numbers_body(request: AddRequest):
    return MathResult(result=request.a + request.b)


@router.get("/divide/{a}/{b}")
def divide_numbers(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}
