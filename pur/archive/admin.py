from django.contrib import admin

from .models import ArchiveItem, Topic, Source, MediaType, MediaFormat

class ArchiveItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['orig_filename', 'orig_url', 'title', 'media_format', 
            'slug', 'thumb_file', 'city', 'street_address', 'district', 'description', 
            'source', 'alt_text', ('creation_year', 'circa', 'decade'),          
             'topics', 'persons', ]}),
        ('Behind the scenes',   {'fields': [('status_num', 'priority'), 'authored_by']}), 
            # , 'classes': ['collapse']
            # 
    ]
    filter_horizontal = ['persons', 'topics']
    list_display = ('title', 'image_img', 'city', 
        'short_media_format', 'creation_year', 'status_num', 'priority' )
    # 'has_address',
    list_filter     = ['city', 'media_format__media_type', 'topics', 'status_num']
    # 'location__city', 

    search_fields = ['orig_filename', 'title', 'slug']

    # Sidelined - not currently used
    def has_address(self, obj):
        if (obj.street_address):
            return True
        else:
            return False
    has_address.short_description = 'Addr'
    has_address.boolean = True

    def short_media_format(self, obj):
        return obj.media_format.slug
    short_media_format.short_description = 'Format'


class SourceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug', 'contact_name', 'contact_email']})
    ]
    list_display = ('title', 'slug', 'contact_name')


class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug']})
    ]
    list_display = ('title', 'slug')


class MediaTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug']})
    ]
    list_display = ('title', 'slug')


class MediaFormatAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['media_type', 'title', 'slug']})
    ]
    list_display = ('title', 'slug')


admin.site.register(ArchiveItem, ArchiveItemAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(MediaType, MediaTypeAdmin)
admin.site.register(MediaFormat, MediaFormatAdmin)


