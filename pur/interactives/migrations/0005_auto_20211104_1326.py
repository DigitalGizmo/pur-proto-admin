# Generated by Django 3.2.2 on 2021-11-04 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactives', '0004_auto_20211103_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotspot',
            options={'ordering': ['interactive_part', 'ordinal']},
        ),
        migrations.AlterModelOptions(
            name='interactivepart',
            options={'ordering': ['interactive', 'slug'], 'verbose_name': 'Part'},
        ),
    ]
