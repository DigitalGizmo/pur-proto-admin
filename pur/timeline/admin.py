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
    list_display = ('title', 'slug', 'ordinal')

class TimelineEntryAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': [
        'timeline_layer', 'year', 'blurb',
        ('has_cell_image', 'priority'), 'thrulines', 
        ('more_text', 'has_more'),
        ('used_in', 'used_in_title')
        ]})
        # 'cell_image_ref',
    ]
    list_display = ('year', 'timeline_layer', 'priority', 'blurb')
    filter_horizontal = ['thrulines',]
    list_filter = ['timeline_layer']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':50})},
    }

admin.site.register(TimelineLayer, TimelineLayerAdmin)
admin.site.register(Thruline, ThrulineAdmin)
admin.site.register(TimelineEntry, TimelineEntryAdmin)
