from django.contrib import admin
from .models import TimelineLayer, Thruline

class TimelineLayerAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': [('slug', 'ordinal'), 'title' ]})
  ]
list_display = ('title', 'ordinal', 'slug')

class ThrulineAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': [('slug', 'ordinal'), 'title' ]})
  ]
list_display = ('title', 'ordinal', 'slug')

admin.site.register(TimelineLayer, TimelineLayerAdmin)
admin.site.register(Thruline, ThrulineAdmin)
