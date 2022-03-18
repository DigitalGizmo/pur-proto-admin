# Generated by Django 3.2.2 on 2022-03-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thruline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=48, unique=True, verbose_name='short name')),
                ('ordinal', models.IntegerField(default=9)),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['ordinal'],
            },
        ),
        migrations.CreateModel(
            name='TimelineLayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=48, unique=True, verbose_name='short name')),
                ('ordinal', models.IntegerField(default=9)),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['ordinal'],
            },
        ),
    ]