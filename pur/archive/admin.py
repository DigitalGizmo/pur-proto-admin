from django.contrib import admin

from .models import ArchiveItem, Topic, Source, MediaType
#, MediaFormat

class ArchiveItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['orig_filename', 'orig_url', 'title', 'slug',   
            'thumb_file', 'description', 'source', 'alt_text', 
            ('creation_year', 'circa', 'decade'),          
             'topics','location', 'persons', ]}),
        ('Behind the scenes',   {'fields': [('status_num', 'priority'), 'authored_by']}), 
            # , 'classes': ['collapse']
    ]
    filter_horizontal = ['persons', 'topics']
    # list_display = ('slug', 'image_img', 'city_', 'district_',
    #    'status_num', 'priority' )
    list_display = ('slug', 'image_img', 'location', 'creation_year',
       'status_num', 'priority' )
    list_filter     = ['location__city', 'topics', 'status_num']
    search_fields = ['orig_filename', 'title', 'slug']



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


# class MediaFormatAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['title', 'slug']})
#     ]
#     list_display = ('title', 'slug')


admin.site.register(ArchiveItem, ArchiveItemAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(MediaType, MediaTypeAdmin)
# admin.site.register(MediaFormat, MediaFormatAdmin)


