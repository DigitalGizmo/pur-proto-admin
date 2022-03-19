from django.contrib import admin
from .models import TimelineLayer, Thruline, TimelineEntry
from django.forms import Textarea, TextInput
from django.db import models

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

class TimelineEntryAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': [
        'timeline_layer', 'year', 'blurb',
        'has_cell_image', 'cell_image_ref',
        'thrulines', 'more_text'
        ]})
    ]
    list_display = ('year', 'timeline_layer', 'blurb')
    filter_horizontal = ['thrulines',]
    list_filter = ['timeline_layer']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':50})},
    }

admin.site.register(TimelineLayer, TimelineLayerAdmin)
admin.site.register(Thruline, ThrulineAdmin)
admin.site.register(TimelineEntry, TimelineEntryAdmin)
