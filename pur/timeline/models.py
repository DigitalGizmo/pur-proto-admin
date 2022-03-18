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
    timeline_layer = models.ForeignKey(
        TimelineLayer,
        related_name='timelineEntries',
        default=0,
        on_delete=models.PROTECT
    )
    year = models.IntegerField(default=1900)
    # title = models.CharField(max_length=64, null=True, blank=True)
    blurb = models.CharField(max_length=194)
    has_cell_image = models.BooleanField(default=False)
    cell_image_ref = models.CharField(max_length=128, null=True, blank=True)
    more_text = models.TextField(null=True, blank=True)
    # has_more_image = models.BooleanField(default=False)
    # more_image_ref = models.CharField(max_length=128, null=True, blank=True)
    thrulines = models.ManyToManyField(Thruline, blank=True)

  