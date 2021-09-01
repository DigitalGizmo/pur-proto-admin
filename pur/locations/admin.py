from django.contrib import admin

from .models import District, Location

class DistrictAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('city', 'after_devel'), 'title', 'description']})
    ]
    list_display = ('title', 'city', 'after_devel' )
    list_filter     = ['city']

class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['level', 'city', 'district', ('street_number',
            'street'), ('lat', 'lng')]})
    ]
    list_display = ('city', 'level', 'district', 'street')
    list_filter     = ['city']

admin.site.register(District, DistrictAdmin)
admin.site.register(Location, LocationAdmin)
