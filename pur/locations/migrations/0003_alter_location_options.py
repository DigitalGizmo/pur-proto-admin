# Generated by Django 3.2.2 on 2021-06-11 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20210611_1224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['city', 'level']},
        ),
    ]
