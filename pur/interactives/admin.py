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
        (None, {'fields': ['interactive_part', 'title', 'slug',
            ('text_percent', 'hotspot_x', 'hotspot_y', 'hotspot_r', 
                'blurb', 'more', 'archive_item')
            ]
        }),
    ]
    list_display = ('title', 'interactive_part', 
        'short_percent', 'short_x', 'short_y', 'short_r')
    list_filter = ['interactive_part']

    # def short_ord(self, obj):
    #     return obj.ordinal
    # short_ord.short_description = 'ord'

    def short_percent(self, obj):
        return obj.text_percent
    short_percent.short_description = '%'

    def short_x(self, obj):
        return obj.hotspot_x
    short_x.short_description = 'x'

    def short_y(self, obj):
        return obj.hotspot_y
    short_y.short_description = 'y'

    def short_r(self, obj):
        return obj.hotspot_r
    short_r.short_description = 'r'


admin.site.register(Interactive ,InteractivesAdmin)
admin.site.register(InteractivePart ,InteractivePartsAdmin)
admin.site.register(Hotspot, HotspotAdmin)
