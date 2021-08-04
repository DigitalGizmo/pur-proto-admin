from django.contrib import admin
from .models import Person, Role

class RoleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug']})
    ]
    list_display = ('title', 'slug')


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('first_name', 'last_name'), 
            ('prefix', 'suffix'), 'role', 'cities']})
    ]
    filter_horizontal = ['cities']
    list_display = ('last_name', 'first_name', 'role')

admin.site.register(Role, RoleAdmin)
admin.site.register(Person, PersonAdmin)

