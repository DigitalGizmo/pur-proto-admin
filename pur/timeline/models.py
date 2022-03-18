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


# class TimelineEntry(models.Model):
#     timeline_layer = models.ForeignKey(
#         TimelineLayer,
#         related_name='years',
#         default=1,
#         on_delete=models.PROTECT
#     )
#     year = models.IntegerField(default=1900)
#     title = models.CharField(max_length=64)
#     blurb = models.CharField(max_length=194)
#     hasImage = models.BooleanField(default=False)
#     pop_text = models.TextField(null=True, blank=True)
#     # thrulines = 
  