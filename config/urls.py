from django.urls import include, path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from .schema import schema
from pur import people

urlpatterns = [
    path('people/', include('pur.people.urls')),
    # path('archive/', include('pur.archive.urls')),
    path('graphql/', 
       csrf_exempt(GraphQLView.as_view(graphiql=True)), 
       name='graphql'),
    path('admin/', admin.site.urls),
]
