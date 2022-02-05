from strawberry.django.views import GraphQLView
from django.contrib import admin
from django.urls import include, path
from .schema import schema
from pur import people

urlpatterns = [
    path('people/', include('pur.people.urls')),
    path('archive/', include('pur.archive.urls')),
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
    path('admin/', admin.site.urls),
]
