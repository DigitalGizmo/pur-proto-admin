from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'sub_title', 'grid_intro']})
    ]
    list_display = ('title', 'sub_title' )

admin.site.register(City, CityAdmin)
