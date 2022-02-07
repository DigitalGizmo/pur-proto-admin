from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import ArchiveItem
from pur.cities.models import City

class CityNode(DjangoObjectType):
    class Meta:
        model = City
        filter_fields = ('id', 'title', 'archiveItems')
        interfaces = (relay.Node, )

class ArchiveItemNode(DjangoObjectType):
    class Meta:
        model = ArchiveItem
        filter_fields = {
            'slug' : ['exact', 'icontains'], 
            'title' : ['exact', 'icontains', 'istartswith'],
            'city_id' : ['exact'],
        }
        interfaces = (relay.Node, )

class Query(ObjectType):
    city = relay.Node.Field(CityNode)
    all_cities = DjangoFilterConnectionField(CityNode)

    archive_item = relay.Node.Field(ArchiveItemNode)
    all_archive_items = DjangoFilterConnectionField(ArchiveItemNode)