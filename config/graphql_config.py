from ariadne import QueryType, make_executable_schema, load_schema_from_path
# ObjectType
import pur.interactives.resolvers

type_defs = [
    load_schema_from_path("config/schema.graphql"),
    load_schema_from_path("pur/interactives/schema.graphql"),
]

query = QueryType()
query.set_field("hotspots", pur.interactives.resolvers.resolve_hotspots)

schema = make_executable_schema(type_defs, query)