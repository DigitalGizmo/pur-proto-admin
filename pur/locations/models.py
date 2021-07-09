from django.db import models
from pur.cities.models import City

class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    after_devel = models.BooleanField('After Development', default=False)
    title = models.CharField(max_length=64)
    description = models.CharField('Notes for internal use',
        max_length=255, null=True, blank=True)

    @property
    def before_or_after(self):
        if self.after_devel:
            return "After"
        else:
            return "Before"
    
    def __str__(self):
        return self.city.title + "-" + \
            self.before_or_after + ": " + \
            self.title

    class Meta:
        ordering = ['city', 'after_devel', 'title']


class Location(models.Model):
    CITY = 1
    DISTRICT = 2
    STREET = 3
    ADDRESS = 4

    LEVEL_CHOICES = (
        (CITY, 'City'),
        (DISTRICT, 'District'),
        (STREET, 'Street'),
        (ADDRESS, 'Address'),
    )

    level = models.IntegerField(choices=LEVEL_CHOICES)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE,
        null=True, blank=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    street_number = models.CharField(max_length=24, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    # district is an association

    @property
    def full_location(self):
        location_concatination = self.city.title + " - " + self.get_level_display()
        if self.level==4:
            location_concatination += ": " + self.street_number + " " +\
                self.street
        elif self.level==3:
            location_concatination += ": " + self.street
        return location_concatination

    class Meta:
        ordering = ['city', 'level']
        
    def __str__(self):
        return self.full_location

    class Meta:
        ordering = ['level', 'city']




