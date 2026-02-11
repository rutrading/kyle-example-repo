from pydantic import BaseModel


class AddRequest(BaseModel):
    a: int
    b: int


class MathResult(BaseModel):
    result: int
