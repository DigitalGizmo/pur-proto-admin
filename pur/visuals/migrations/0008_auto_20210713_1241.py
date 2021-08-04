# Generated by Django 3.2.2 on 2021-07-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visuals', '0007_image_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='orig_url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Dropbox URL'),
        ),
        migrations.AddField(
            model_name='image',
            name='thumb_file',
            field=models.ImageField(default='placeholder.jpg', upload_to='visuals/thumbpics'),
        ),
        migrations.AlterField(
            model_name='image',
            name='status_num',
            field=models.IntegerField(choices=[(0, '0 - Initial Entry'), (1, '1 - In Progress'), (2, '2 - Ready for Review'), (3, '3 - Reviewed'), (4, '4 - Candidate for Pub'), (5, '5 - Published')], default=0),
        ),
    ]