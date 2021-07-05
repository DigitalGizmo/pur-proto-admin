from django.contrib import admin

from .models import Image, Topic, Source

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['orig_filename', 'title', 'slug',   
            'description', 'alt_text', ('creation_year', 'circa', 'decade'), 
            'source', 'topics',
            'location', 'persons', ]}),
        ('Behind the scenes',   {'fields': ['status_num', 'priority']}), 
            # , 'classes': ['collapse']
    ]
    filter_horizontal = ['persons', 'topics']
    list_display = ('slug', 'image_img', 'city_', 'district_',
       'status_num', 'priority' )

admin.site.register(Image, ImageAdmin)


admin.site.register(Topic)


admin.site.register(Source)
