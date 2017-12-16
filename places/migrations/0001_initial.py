# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import dotmanca.storage
import places.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sort_order', models.IntegerField()),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('the_image', models.ImageField(blank=True, null=True, storage=dotmanca.storage.OverwriteStorage(), upload_to=places.models.place_image_upload_to)),
            ],
        ),
    ]