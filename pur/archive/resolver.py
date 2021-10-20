from ariadne import QueryType, make_executable_schema
from .models import ArchiveItem

type_defs= """
type Query{
    all_images(city_id: Int): [ArchiveItem]
}
type ArchiveItem {
    id: Int
    slug: String!
    title: String!
    description: String
    creation_year: Int
    source_title: String
    location_display: String
}
"""

query = QueryType()

@query.field('all_images')
def resolve_archive_images(*_, city_id=None): # city=None
    print("city_id: " + str(city_id))
    if city_id:
        return ArchiveItem.objects.filter(media_format__media_type__slug='image',
            status_num__gte=2, priority__gte=1, location__city=city_id)
    return ArchiveItem.objects.filter(media_format__media_type__slug='image',
            status_num__gte=2, priority__gte=1)

schema = make_executable_schema(type_defs, query)
