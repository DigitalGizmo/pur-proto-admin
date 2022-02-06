from ast import Try
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
    all_archiveitems = graphene.List(ArchiveItemType)
    city_by_id = graphene.Field(CityType, 
        id=graphene.Int(required=True))
    images_by_cityid = graphene.List(ArchiveItemType,
        cityid=graphene.Int(required=True))

    def resolve_all_archiveitems(root,info):
        return ArchiveItem.objects.select_related("city").all()

    def resolve_city_by_id(root, info, id):
        try:
            return City.objects.get(id=id)
        except City.DoesNotExist:
            return None

    def resolve_imgages_by_cityid(root, info, cityid):
        try:
            return ArchiveItem.objects.filter(
                media_format__media_type__slug='image',
                status_num__gte=2, priority__gte=1, 
                city=cityid)
        except ArchiveItemType.DoesNotExist:
            return ArchiveItem.objects.all()

schema = graphene.Schema(query=Query)