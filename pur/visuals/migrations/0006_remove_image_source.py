# Generated by Django 3.2.2 on 2021-07-04 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visuals', '0005_auto_20210704_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='source',
        ),
    ]
