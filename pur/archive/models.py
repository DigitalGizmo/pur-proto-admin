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


class MediaType(models.Model):
    slug = models.SlugField(max_length=24, unique=True, default='image')
    title = models.CharField(max_length=32, default='Image')

class MediaFormat(models.Model):
    media_type = models.ForeignKey(MediaType, default='image', on_delete=models.SET_DEFAULT)
    slug = models.SlugField(max_length=24, unique=True, default='photo')
    title = models.CharField(max_length=64)


class ArchiveItem(models.Model):
    STATUS_NUMS = (
        (0,'0 - Initial Entry'),
        (1,'1 - In Progress'),
        (2,'2 - Ready for Review'),
        (3,'3 - Reviewed'),
        (4,'4 - Candidate for Pub'),
        (5,'5 - Published'),
    )
    PRIORITY = (
        (0,'0 - Reference'),
        (1,'1 - Could Use'),
        (2,'2 - Pretty Good'),
        (3,'3 - Golden'),
    )
    AUTHORED_BY = (
        ('','---'),
        ('Ann','Ann'),
        ('Dave','Dave'),
        ('Stacy','Stacy'),
        ('DG','DG'),
    )
    location = models.ForeignKey(Location, 
        default=1, on_delete=models.PROTECT)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL,
        null=True, blank=True)
    slug = models.SlugField('short name', max_length=48, unique=True)
    orig_filename = models.CharField(max_length=128, null=True, blank=True)
    orig_url = models.URLField('Dropbox URL', max_length=255, null=True, blank=True)
    thumb_file = models.ImageField(upload_to='visuals/thumbpics', default='placeholder.jpg')
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField('caption',max_length=255, null=True, blank=True)
    creation_year = models.IntegerField('Year', 
        help_text='creation year', null=True, blank=True)
    circa = models.BooleanField(default=False)
    decade = models.BooleanField(default=False)
    alt_text = models.TextField(null=True, blank=True)
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)
    priority = models.IntegerField(default=0, choices=PRIORITY)
    authored_by = models.CharField(max_length=16, choices=AUTHORED_BY, default='')
    persons = models.ManyToManyField(Person, blank=True)
    topics = models.ManyToManyField(Topic, blank=True)
    media_format = models.ForeignKey(MediaFormat, default='photo', on_delete=models.SET_DEFAULT)


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

    def __str__(self):
        return self.slug

    def image_img(self):
        # return format_html('<img src="/media/visuals/thumbpics/' + self.slug + \
        #             '.jpg" width="75" height="100"/>')    
        return format_html('<img src="' + self.thumb_file.url + '" width="100" />')    
    image_img.short_description = 'Thumb'

    class Meta:
        verbose_name = "Archive Item"
