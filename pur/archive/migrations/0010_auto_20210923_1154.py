# Generated by Django 3.2.2 on 2021-09-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0009_auto_20210804_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Archive Item'},
        ),
        migrations.RemoveField(
            model_name='image',
            name='format',
        ),
        migrations.AlterField(
            model_name='image',
            name='creation_year',
            field=models.IntegerField(blank=True, help_text='creation year', null=True, verbose_name='Year'),
        ),
    ]
