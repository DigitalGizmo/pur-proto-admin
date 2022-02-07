# from graphene import relay, ObjectType
# from graphene_django import DjangoObjectType
# from graphene_django.filter import DjangoFilterConnectionField

# from .models import ArchiveItem
# from pur.cities.models import City

# class CityNode(DjangoObjectType):
#     class Meta:
#         model = City
#         filter_fields = ('id', 'title', 'archiveItems')
#         interfaces = (relay.Node, )

# class ArchiveItemNode(DjangoObjectType):
#     class Meta:
#         model = ArchiveItem
#         filter_fields = {
#             'slug' : ['exact', 'icontains'], 
#             'title' : ['exact', 'icontains', 'istartswith'],
#             'city_id' : ['exact'],
#         }
#         interfaces = (relay.Node, )

# class Query(ObjectType):
#     city = relay.Node.Field(CityNode)
#     all_cities = DjangoFilterConnectionField(CityNode)

#     archive_item = relay.Node.Field(ArchiveItemNode)
#     all_archive_items = DjangoFilterConnectionField(ArchiveItemNode)

# For now, filter directly by city_id rather than the
# Relay node approach above
# Next frontier: how to filter by Topic (many to many)
# as well. Look at past searches for double underscore,
# "and" search in other projects

import graphene
from graphene_django import DjangoObjectType
from pur.archive.models import ArchiveItem, Source
from pur.cities.models import City
from pur.locations.models import District

class CityType(DjangoObjectType):
    class Meta:
        model = City
        fields = ("id", "title", "archiveItems")

class SourceType(DjangoObjectType):
    class Meta:
        model = Source
        fields = ("title", )

class DistrictType(DjangoObjectType):
    class Meta:
        model = District
        fields = ("title", )

class ArchiveItemType(DjangoObjectType):
    class Meta:
        model = ArchiveItem
        fields = ("id", "slug", "title", "city", 
            "description", "creation_year", "source", 
            "street_address", "district", )

class Query(graphene.ObjectType):
    # all_archiveitems = graphene.List(ArchiveItemType)
    city_by_id = graphene.Field(CityType, 
        id=graphene.Int(required=True))
    visual_record = graphene.List(ArchiveItemType,
        city_id=graphene.Int(required=False))

    # def resolve_all_archiveitems(root,info):
    #     return ArchiveItem.objects.select_related("city").all()

    def resolve_city_by_id(root, info, id):
        try:
            return City.objects.get(id=id)
        except City.DoesNotExist:
            return None

    # def resolve_images_by_id(root, info, id):
    def resolve_visual_record(root, info, **kwargs):
        city_id = kwargs.get('city_id')
        if city_id:
            return ArchiveItem.objects.filter(city_id=city_id)
        return ArchiveItem.objects.all()
 