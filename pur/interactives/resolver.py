from ariadne import QueryType, make_executable_schema
from .models import Hotspot

type_defs= """
type Query{
    hotspots(interactive_id: Int): [Hotspot]
}
type Hotspot {
    id: Int
    ordinal: Int
    title: String!
    blurb: String
    text_percent: Int
    hotspot_x: Int
    hotspot_y: Int
    hotspot_r: Int
}
"""

query = QueryType()

@query.field('hotspots')
def resolve_hotspots(*_, interactive_id=None): # city=None
    print("interactive_id: " + str(interactive_id))
    if interactive_id:
        return Hotspot.objects.filter(interactive=interactive_id)
    return Hotspot.objects.all()

schema = make_executable_schema(type_defs, query)
