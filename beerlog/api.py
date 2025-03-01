from typing import List, Optional
from fastapi import FastAPI, Response, status  # protocol: ASGI
from beerlog.core import get_beers_from_database
from beerlog.database import get_session
from beerlog.serializers import BeerOut, BeerIn
from beerlog.models import Beer


api = FastAPI(title="Beerlog API", version="0.1.0")


@api.get("/beers", response_model=List[BeerOut])
async def list_beers(style: Optional[str] = None):
    beers = get_beers_from_database(style)
    return beers


@api.post("/beers", response_model=BeerOut)
async def add_beer(beer_in: BeerIn, response: Response):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    response.status_code = status.HTTP_201_CREATED
    return beer
