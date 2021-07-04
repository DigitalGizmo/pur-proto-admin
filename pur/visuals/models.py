from django.db import models
from django.utils.html import format_html
from pur.people.models import Person
from pur.locations.models import Location

class CommonVisuals(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
        null=True, blank=True)
    slug = models.SlugField('short name', max_length=48, unique=True)
    orig_filename = models.CharField(max_length=128, null=True, blank=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    creation_year = models.IntegerField(null=True, blank=True)
    circa = models.BooleanField(default=False)
    source = models.CharField(max_length=128, null=True, blank=True)
    alt_text = models.CharField(max_length=128, null=True, blank=True)
    persons = models.ManyToManyField(Person, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug


class Image(CommonVisuals):
    PHOTO = 'photo'
    GRAPHIC = 'graph'
    DRAWING = 'draw'
    MAP = 'map'
    DOCUMENT = 'doc'

    FORMAT_CHOICES = (
        (PHOTO, 'photo'),
        (GRAPHIC, 'graphic/ephemera'),
        (DRAWING, 'drawing'),
        (MAP, 'map'),
        (DOCUMENT, 'document'),
    )

    format = models.CharField(max_length=5, choices=FORMAT_CHOICES)

    def image_img(self):
        return format_html('<img src="/static/visuals/images/thumbs/' + self.slug + \
                    '.jpg" width="75" height="100"/>')    
    image_img.short_description = 'Thumb'


class Topic(models.Model):
    slug = models.SlugField('short name', max_length=48, unique=True)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.slug


class Source(models.Model):
    slug = models.SlugField('short name', max_length=48, unique=True)
    title = models.CharField(max_length=64)
    contact_name = models.CharField(max_length=64, null=True, blank=True)
    contact_email = models.CharField(max_length=64, null=True, blank=True)


    def __str__(self):
        return self.slug
