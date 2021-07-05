from django.db import models
from django.utils.html import format_html
from pur.people.models import Person
from pur.locations.models import Location

class Source(models.Model):
    slug = models.SlugField('short name', max_length=48, unique=True)
    title = models.CharField(max_length=64)
    contact_name = models.CharField(max_length=64, null=True, blank=True)
    contact_email = models.CharField(max_length=64, null=True, blank=True)


    def __str__(self):
        return self.slug

class Topic(models.Model):
    slug = models.SlugField('short name', max_length=48, unique=True)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.slug


class CommonVisuals(models.Model):
    STATUS_NUMS = (
        (0,'0 - Initial Entry'),
        (1,'1 - In Admin Only'),
        (2,'2 - Development (Wireframe)'),
        (3,'3 - Candidate for Publication'),
        (4,'4 - Published'),
    )
    PRIORITY = (
        (0,'0 - Reference'),
        (1,'1 - Could Use'),
        (2,'2 - Pretty Good'),
        (3,'3 - Golden'),
    )
    location = models.ForeignKey(Location, 
        default=1, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL,
        null=True, blank=True)
    slug = models.SlugField('short name', max_length=48, unique=True)
    orig_filename = models.CharField(max_length=128, null=True, blank=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField('caption',max_length=255, null=True, blank=True)
    creation_year = models.IntegerField(null=True, blank=True)
    circa = models.BooleanField(default=False)
    decade = models.BooleanField(default=False)
    alt_text = models.CharField(max_length=128, null=True, blank=True)
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)
    priority = models.IntegerField(default=0, choices=PRIORITY)
    persons = models.ManyToManyField(Person, blank=True)
    topics = models.ManyToManyField(Topic, blank=True)

   # City title
    @property
    def city_(self):
        return self.location.city.title

   # District
    @property
    def district_(self):
        if self.location.district:
            return self.location.district.title
        else:
            return ""

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug


class Image(CommonVisuals):
    PHOTO = 'photo'
    GRAPHIC = 'graph'
    DRAWING = 'draw'
    MAP = 'map'
    DOCUMENT = 'doc'

    FORMAT_CHOICES = (
        (PHOTO, 'photo'),
        (GRAPHIC, 'graphic/ephemera'),
        (DRAWING, 'drawing'),
        (MAP, 'map'),
        (DOCUMENT, 'document'),
    )

    format = models.CharField(max_length=5, choices=FORMAT_CHOICES)

    def image_img(self):
        return format_html('<img src="/static/visuals/images/thumbs/' + self.slug + \
                    '.jpg" width="75" height="100"/>')    
    image_img.short_description = 'Thumb'

