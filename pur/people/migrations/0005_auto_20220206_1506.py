# Generated by Django 3.2.2 on 2022-02-06 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20210804_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['title']},
        ),
    ]
