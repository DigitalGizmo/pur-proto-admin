import graphene

import pur.archive.schema
import pur.interactives.schema
import pur.timeline.schema

class Query(
    pur.archive.schema.Query,
    pur.interactives.schema.Query,
    pur.timeline.schema.Query,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    pass

schema = graphene.Schema(query=Query)
# print(str(schema))