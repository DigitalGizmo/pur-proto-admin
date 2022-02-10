from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Interactive, InteractivePart, Hotspot
# from pur.cities.models import City

class InteractiveNode(DjangoObjectType):
    class Meta:
        model = Interactive
        filter_fields = ['id', 'slug']
        interfaces = (relay.Node, )

class InteractivePartNode(DjangoObjectType):
    class Meta:
        model = InteractivePart
        filter_fields = ['slug', 'interactive_id']
        interfaces = (relay.Node, )

class HotspotNode(DjangoObjectType):
    class Meta:
        model = Hotspot
        filter_fields = ['interactive_part_id', 'title']
        interfaces = (relay.Node, )

class Query(ObjectType):
    interactive = relay.Node.Field(InteractiveNode)
    all_interactives = DjangoFilterConnectionField(InteractiveNode)

    interactive_part = relay.Node.Field(InteractivePartNode)
    all_interactive_parts = DjangoFilterConnectionField(InteractivePartNode)