from ariadne import QueryType, make_executable_schema
from .models import ArchiveItem

type_defs= """

type Query{
    all_images: [ArchiveItem]
}

type ArchiveItem {
    id: ID
    slug: String!
    title: String!

}

"""

query = QueryType()

@query.field('all_images')
def resolve_archive_images(*_):
    return ArchiveItem.objects.filter(media_format__media_type__slug='image')

schema = make_executable_schema(type_defs, query)
