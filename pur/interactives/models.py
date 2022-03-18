from django.db import models
from pur.cities.models import City
from pur.archive.models import ArchiveItem

class Interactive(models.Model):
    city = models.ForeignKey(City, 
        default=1, on_delete=models.PROTECT)
    slug = models.SlugField('short name', max_length=48, unique=True)
    title = models.CharField(max_length=64)
    blurb = models.TextField('menu blurb', null=True, blank=True)

    def __str__(self):
        return self.slug

class InteractivePart(models.Model):
    interactive = models.ForeignKey(Interactive, 
        related_name='interactiveParts', default=1, 
        on_delete=models.PROTECT)
    slug = models.SlugField('short name', max_length=48, unique=True)
    part_num = models.IntegerField(default=99)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.slug

    class Meta:
        # verbose_name = "Part"
        ordering = ['interactive', 'slug']


class Hotspot(models.Model):
    interactive_part = models.ForeignKey(InteractivePart,
        related_name='hotspots', default=1, on_delete=models.PROTECT)
    # Presence of an archive item triggers image in more pop.
    archive_item = models.ForeignKey(ArchiveItem,
        related_name='hotspots', on_delete=models.SET_NULL,
        null=True, blank=True)
    ordinal = models.IntegerField(default=99)
    title = models.CharField(max_length=64)
    slug = models.SlugField('short name', max_length=48,
        null=True, blank=True)
    text_percent = models.IntegerField('text position %', default=90)
    hotspot_x = models.IntegerField(default=900)
    hotspot_y = models.IntegerField(default=90)
    hotspot_r = models.IntegerField('hotspot radius',default=20)
    blurb = models.TextField( null=True, blank=True)
    more = models.TextField( null=True, blank=True)
    zoom_percent = models.IntegerField( default=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['interactive_part', 'text_percent']
