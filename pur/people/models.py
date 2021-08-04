from django.db import models
from pur.cities.models import City

class Role(models.Model):
    slug = models.SlugField('short name', max_length=32, unique=True)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Primary Role"


class Person(models.Model):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,
        null=True, blank=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    prefix = models.CharField(max_length=16, null=True, blank=True)
    suffix = models.CharField(max_length=16, null=True, blank=True)
    cities = models.ManyToManyField(City, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

