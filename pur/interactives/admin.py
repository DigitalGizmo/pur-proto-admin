from django.contrib import admin

from .models import Interactive, InteractivePart, Hotspot

class InteractivesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['city', 'slug', 'title', 'blurb']
        }),
    ]
    list_display = ('city', 'slug', 'title')

class InteractivePartsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['interactive', 'slug', 'title']
        }),
    ]
    list_display = ('slug', 'title', 'interactive')

class HotspotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['interactive', 'ordinal', 'title', 
            ('text_percent', 'hotspot_x', 'hotspot_y', 'hotspot_r', 
                'blurb', 'more')
            ]
        }),
    ]
    list_display = ('title', 'ordinal', 
        'text_percent', 'hotspot_x', 'hotspot_y', 'hotspot_r')
    list_filter = ['interactive']

admin.site.register(Interactive ,InteractivesAdmin)
admin.site.register(InteractivePart ,InteractivePartsAdmin)
admin.site.register(Hotspot, HotspotAdmin)
