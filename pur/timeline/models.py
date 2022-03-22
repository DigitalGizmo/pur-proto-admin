from django.db import models

class TimelineLayer(models.Model):
    slug = models.SlugField('short name', max_length=48, unique=True)
    ordinal = models.IntegerField(default=9)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title
    class Meta:
      ordering = ['ordinal']

class Thruline(models.Model):
    slug = models.SlugField('short name', max_length=48, unique=True)
    ordinal = models.IntegerField(default=9)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title
    class Meta:
      ordering = ['ordinal']


class TimelineEntry(models.Model):
    PRIORITY = (
        (1,'1 - Probably Not'),
        (2,'2 - Maybe'),
        (3,'3 - For sure'),
    )    
    timeline_layer = models.ForeignKey(
        TimelineLayer,
        related_name='timelineEntries',
        default=0,
        on_delete=models.PROTECT
    )
    year = models.IntegerField(default=1900)
    # title = models.CharField(max_length=64, null=True, blank=True)
    blurb = models.TextField()
    has_cell_image = models.BooleanField(default=False)
    cell_image_ref = models.CharField(max_length=128, null=True, blank=True)
    more_text = models.TextField(null=True, blank=True)
    priority = models.IntegerField(default=3, choices=PRIORITY)
    has_more = models.BooleanField(default=False)
    # has_more_image = models.BooleanField(default=False)
    # more_image_ref = models.CharField(max_length=128, null=True, blank=True)
    thrulines = models.ManyToManyField(Thruline, blank=True)
    used_in = models.CharField(max_length=64, null=True, blank=True,
        help_text='e.g.: people/haines-dauner')
    used_in_title = models.CharField(max_length=128, null=True, blank=True,
        help_text='e.g.: Bob Haines and Gene Dauner, Photographers')
    class Meta:
      ordering = ['timeline_layer', 'year']