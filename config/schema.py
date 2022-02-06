import graphene
from graphene_django import DjangoObjectType
# from graphene_django.filter import DjangoFilterConnectionField
# from graphene import relay, ObjectType

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
    images_by_id = graphene.List(ArchiveItemType,
        id=graphene.Int(required=True))

    def resolve_all_archiveitems(root,info):
        return ArchiveItem.objects.select_related("city").all()

    def resolve_city_by_id(root, info, id):
        try:
            return City.objects.get(id=id)
        except City.DoesNotExist:
            return None

    # def resolve_images_by_id(root, info, id):
    def resolve_images_by_id(root, info, **kwargs):
        # try:
        id = kwargs.get('id')
        return ArchiveItem.objects.get(id=id)
            # return ArchiveItem.objects.select_related("city").all()
        # except ArchiveItem.DoesNotExist:
        #     return None

# class CityNode(DjangoObjectType):
#     class Meta:
#         model = City
#         filter_fields = ('title', 'archiveItems')
#         interfaces = (relay.Node, )

    # class ArchiveItemNode(DjangoObjectType):
    #     class Meta:
    #         model = ArchiveItem
    #         filter_fields = {
    #             'slug' : ['exact', 'icontains'], 
    #             'title' : ['exact', 'icontains', 'istartswith'],
    #             'city__id' : ['exact'],
    #         }
    #         interfaces = (relay.Node, )

schema = graphene.Schema(query=Query)