from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    prefix = models.CharField(max_length=16, null=True, blank=True)
    suffix = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
