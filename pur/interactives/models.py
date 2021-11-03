from django.db import models
from pur.cities.models import City

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
        default=1, on_delete=models.PROTECT)
    slug = models.SlugField('short name', max_length=48, unique=True)
    part_num = models.IntegerField(default=99)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.slug


class Hotspot(models.Model):
    # interactive_part = models.ForeignKey(InteractivePart,
    #     default=1, on_delete=models.PROTECT)
    interactive = models.ForeignKey(Interactive,
        default=1, on_delete=models.PROTECT)
    ordinal = models.IntegerField(default=99)
    title = models.CharField(max_length=64)
    text_percent = models.IntegerField(default=90)
    hotspot_x = models.IntegerField(default=900)
    hotspot_y = models.IntegerField(default=90)
    hotspot_r = models.IntegerField(default=20)
    blurb = models.TextField( null=True, blank=True)
    more = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['ordinal']
