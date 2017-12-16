# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('sort_order', models.IntegerField()),
                ('the_image', models.ImageField(upload_to='')),
                ('added_timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery')),
            ],
        ),
    ]