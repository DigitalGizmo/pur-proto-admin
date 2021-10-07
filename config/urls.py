from django.contrib import admin
from django.urls import include, path
from pur import people

urlpatterns = [
    path('people/', include('pur.people.urls')),
    path('archive/', include('pur.archive.urls')),
    path('admin/', admin.site.urls),
]
