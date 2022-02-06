from pyexpat import model
from unicodedata import name
import graphene
from graphene_django import DjangoObjectType

from pur.archive.models import ArchiveItem
from pur.cities.models import City

class CityType(DjangoObjectType):
    class Meta:
        model = City
        fields = ("id", "title", "archiveItems")

class ArchiveItemType(DjangoObjectType):
    class Meta:
        model = ArchiveItem
        fields = ("id", "slug", "title", "city")

class Query(graphene.ObjectType):
    images = graphene.List(ArchiveItemType)
    city_by_name = graphene.Field(CityType, 
        title=graphene.String(required=True))

    def resolve_images(root,info):
        return ArchiveItem.objects.select_related("city").all()

    def resolve_city_by_name(root, info):
        try:
            return City.objects.get(title=title)
        except City.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)