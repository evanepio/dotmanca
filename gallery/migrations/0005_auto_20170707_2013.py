# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 23:13
from __future__ import unicode_literals

from django.db import migrations, models

import dotmanca.storage
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20170705_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='the_image',
            field=models.ImageField(storage=dotmanca.storage.OverwriteStorage(), upload_to=gallery.models.gallery_image_upload_to),
        ),
    ]
