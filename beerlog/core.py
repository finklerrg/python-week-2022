from typing import List
from sqlmodel import select
from beerlog.database import get_session
from beerlog.models import Beer


def add_beer_to_database(
    name: str, style: str, flavor: int, image: int, cost: int
) -> bool:
    """Adds a beer to the database."""
    with get_session() as session:
        beer = Beer(
            name=name, style=style, flavor=flavor, image=image, cost=cost
        )
        session.add(beer)
        session.commit()
        return True


def get_beers_from_database(style: str = None) -> List[Beer]:
    """Returns a list of beers from the database."""
    with get_session() as session:
        sql_query = select(Beer)
        beers = session.exec(sql_query)
        return list(beers)
