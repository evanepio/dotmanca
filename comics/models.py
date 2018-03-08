from django.db import models

from dotmanca.storage import OverwriteStorage


def arc_image_upload_to(instance, file_name):
    file_extension = file_name.split(".")[-1]
    return F'galleries/{instance.slug}.{file_extension}'


class Arc(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField()
    the_image = models.ImageField(null=False, blank=False, upload_to=arc_image_upload_to,
                                  storage=OverwriteStorage())


def issue_image_upload_to(instance, file_name):
    file_extension = file_name.split(".")[-1]
    return F'galleries/{instance.arc.slug}/{instance.slug}.{file_extension}'


class Issue(models.Model):
    arc = models.ForeignKey(Arc, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField()
    the_image = models.ImageField(null=False, blank=False, upload_to=arc_image_upload_to,
                                  storage=OverwriteStorage())