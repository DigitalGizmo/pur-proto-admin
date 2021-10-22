from django.contrib import admin

from .models import ArchiveItem, Topic, Source, MediaType, MediaFormat

class ArchiveItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['orig_filename', 'orig_url', 'title', 'media_format', 
            'slug', 'thumb_file', 'description', 'source', 'alt_text', 
            ('creation_year', 'circa', 'decade'),          
             'topics','location', 'persons', ]}),
        ('Behind the scenes',   {'fields': [('status_num', 'priority'), 'authored_by']}), 
            # , 'classes': ['collapse']
            # 
    ]
    filter_horizontal = ['persons', 'topics']
    list_display = ('slug', 'image_img', 'short_media_format', 'short_location', 'creation_year',
       'status_num', 'priority' )
    list_filter     = ['media_format__media_type', 'topics', 'status_num']
    # 'location__city', 
    search_fields = ['orig_filename', 'title', 'slug']

    def short_location(self, obj):
        return obj.location.city.title + ": " + obj.location.get_level_display()
    short_location.short_description = 'Location'

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


