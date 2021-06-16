from django.contrib import admin

from .models import Image

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ['persons']

admin.site.register(Image, ImageAdmin)
