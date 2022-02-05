import strawberry_django
from . import models

@strawberry_django.type(models.Hotspot)
class Hotspot:
  id: int
  ordinal: int
  title: str
