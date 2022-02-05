import strawberry
from typing import List
from .types import Hotspot

@strawberry.type
class Query:
  hotspots: List[Hotspot] = strawberry.django.field()

schema = strawberry.Schema(query=Query)