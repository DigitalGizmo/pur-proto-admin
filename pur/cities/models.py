from django.db import models

class City(models.Model):
    title = models.CharField(max_length=32)
    sub_title = models.CharField(max_length=128, null=True, blank=True)
    grid_intro = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
