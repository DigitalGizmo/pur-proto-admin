from django.contrib import admin

from .models import Image

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['orig_filename', 'title', 'slug',   
            'description', 'alt_text', ('creation_year', 'circa'), 'source',
            'location', 'persons', ]}),
    ]
    filter_horizontal = ['persons']
    list_display = ('title', 'slug', 'image_img', 'orig_filename', 'location',
        )

admin.site.register(Image, ImageAdmin)
