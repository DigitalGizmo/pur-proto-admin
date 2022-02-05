import strawberry_django
from . import models

@strawberry_django.type(models.ArchiveItem)
class ArchiveItem:
    id: int
    slug: str
    title: str
    description: str
    