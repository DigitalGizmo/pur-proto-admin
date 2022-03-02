from django.db import models

# class TimelineLayer(models.Model):
#     title = models.CharField(max_length=32)
#     class_name = models.CharField(max_length=32)
#     ordinal = models.IntegerField(default=9)

#     def __str__(self):
#         return self.title    

# # class Thruline

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
  