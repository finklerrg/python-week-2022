from datetime import datetime
from pydantic import BaseModel, validator
from fastapi import HTTPException, status


class BeerOut(BaseModel):
    id: int
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int
    date: datetime


class BeerIn(BaseModel):
    name: str
    style: str
    flavor: int
    image: int
    cost: int

    @validator("flavor", "image", "cost")
    def validateRatings(cls, v, field):
        if v < 0 or v > 10:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"{field.name} must be between 0 and 10")
        return v
