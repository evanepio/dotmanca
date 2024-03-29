# Generated by Django 4.1 on 2022-08-19 17:56

import comics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0006_auto_20200208_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arc',
            name='the_image',
            field=models.ImageField(upload_to=comics.models.arc_image_upload_to),
        ),
        migrations.AlterField(
            model_name='issue',
            name='the_image',
            field=models.ImageField(upload_to=comics.models.arc_image_upload_to),
        ),
    ]
