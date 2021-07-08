from django.contrib import admin

from .models import Person, Role

admin.site.register(Person)

admin.site.register(Role)
