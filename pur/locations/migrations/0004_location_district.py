# Generated by Django 3.2.2 on 2021-06-14 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_alter_location_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.district'),
        ),
    ]
