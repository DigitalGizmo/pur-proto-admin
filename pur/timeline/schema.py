from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import TimelineLayer, Thruline, TimelineEntry

class TimelineLayerNode(DjangoObjectType):
    class Meta:
        model = TimelineLayer
        filter_fields = ['slug', 'ordinal']
        interfaces = (relay.Node, )

class ThrulineNode(DjangoObjectType):
    class Meta:
        model = Thruline
        filter_fields = ['slug', 'ordinal']
        interfaces = (relay.Node, )

class TimelineEntryNode(DjangoObjectType):
    class Meta:
        model = TimelineEntry
        filter_fields = ['timeline_layer_id', 'year']
        interfaces = (relay.Node, )

class Query(ObjectType):
    # interactive = relay.Node.Field(InteractiveNode)
    # all_interactives = DjangoFilterConnectionField(InteractiveNode)

    # interactive_part = relay.Node.Field(InteractivePartNode)
    # all_interactive_parts = DjangoFilterConnectionField(InteractivePartNode)
    timeline_layers = DjangoFilterConnectionField(TimelineLayerNode)