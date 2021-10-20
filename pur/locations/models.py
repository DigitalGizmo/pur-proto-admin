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
    # These location strings show up in the Image/Location dropdown 
    # as well as in the Locations/District list
    def full_location(self):
        location_concatination = self.city.title + " - " + self.get_level_display()
        if self.level==4: # Address
            location_concatination += ": " + self.street_number + " " +\
                self.street
        elif self.level==3: # Street
            location_concatination += ": " + self.street
        elif self.level==2: # District
            location_concatination += ": " + self.district.title
        return location_concatination

    @property
    # Display for Visual Record. "Regular" address format
    def location_display(self):
        # print("-- location_display level: " + str(self.level))
        location_concatination = " "
        if self.level==4: # Address
            # print("--- in 4 ")
            location_concatination += str(self.street_number) + " " + self.street + ", "
        elif self.level==3: # Street
            # print("--- in 3 ")
            location_concatination += self.street + ", "
        elif self.level==2: # District
            # print("--- in 2 ")
            location_concatination += self.district.title + ", "
        location_concatination += self.city.title
        # print("-- location_concatination pre area: " + location_concatination)
        # Not sure why, but this breaks address -- no location shows
        # if (self.level > 2 and self.district.title):
        #     print("--- in > 2 ")
        #     location_concatination += ", " + self.district.title + " area"
        #     # return location_concatination
        # print("-- location_concatination post area: " + location_concatination)
        return location_concatination

    class Meta:
        ordering = ['city', 'level']
        
    def __str__(self):
        return self.full_location

    class Meta:
        ordering = ['level', 'city']




