# Generated by Django 3.2.2 on 2021-10-22 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_city_options'),
        ('locations', '0006_alter_location_options'),
        ('archive', '0015_archiveitem_media_format'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mediatype',
            options={'ordering': ['slug']},
        ),
        migrations.AddField(
            model_name='archiveitem',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cities.city'),
        ),
        migrations.AddField(
            model_name='archiveitem',
            name='street_address',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='archiveitem',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.location'),
        ),
    ]