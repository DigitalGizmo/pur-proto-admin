import strawberry
from typing import List
from pur.interactives.types import Hotspot
from pur.archive.types import ArchiveItem

@strawberry.type
class Query:
  hotspots: List[Hotspot] = strawberry.django.field()
  all_images: List[ArchiveItem] = strawberry.django.field()

schema = strawberry.Schema(query=Query)