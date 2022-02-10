import graphene

import pur.archive.schema
import pur.interactives.schema

class Query(
    pur.archive.schema.Query,
    pur.interactives.schema.Query ,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    pass

schema = graphene.Schema(query=Query)
# print(str(schema))