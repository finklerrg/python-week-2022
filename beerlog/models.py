from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select


class Beer(SQLModel, table=True):
    id: int =Field(primary_key=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int


brewdog = Beer(name="Brew Dog", style="NEIPA", flavor=6, image=8, cost=8)
