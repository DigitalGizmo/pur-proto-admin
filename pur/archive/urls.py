from django.urls import include, path
from ariadne_django.views import GraphQLView
from .resolver import schema

urlpatterns = [
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql')
]
