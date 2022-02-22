import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
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
        city_id=graphene.Int(required=False),
        media_format_ids=graphene.List(graphene.Int, required=False)
        )

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
        media_format_ids = kwargs.get('media_format_ids')

        qquery = Q(status_num__gte=2, priority__gte=1)

        # Narrow the basic query with city id, if given
        if city_id:
            qquery.add((Q(city_id=city_id)), 'AND')

        # Create a batch of Format ORs
        if media_format_ids:
            fquery = Q()
            for format_id in media_format_ids:
                fquery.add((Q(media_format_id=format_id)), 'OR')
            # And them to the existing query
            qquery.add(fquery, 'AND')

        return ArchiveItem.objects.filter(qquery)

        # if city_id:
        #     if media_format_id:
        #         return ArchiveItem.objects.filter(
        #         status_num__gte=2, priority__gte=1, city_id=city_id,
        #         media_format_id=media_format_id)
        #     return ArchiveItem.objects.filter(
        #         status_num__gte=2, priority__gte=1, city_id=city_id)
        # if media_format_id and not city_id:
        #         return ArchiveItem.objects.filter(
        #         status_num__gte=2, priority__gte=1,
        #         media_format_id=media_format_id)
        # return ArchiveItem.objects.filter(
        #     # media_format__media_type__slug='image',
        #     status_num__gte=2, priority__gte=1)
