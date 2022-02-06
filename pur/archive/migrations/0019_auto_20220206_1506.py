# Generated by Django 3.2.2 on 2022-02-06 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_city_options'),
        ('archive', '0018_alter_archiveitem_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='archiveitem',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='archiveItems', to='cities.city'),
        ),
    ]
