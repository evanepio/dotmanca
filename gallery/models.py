from django.db import models
from django.urls import reverse

from dotmanca.storage import OverwriteStorage


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    added_timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField()

    def get_absolute_url(self):
        kwargs = {"slug": self.slug}
        return reverse("gallery:gallery", kwargs=kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "galleries"


def gallery_image_upload_to(instance, file_name):
    file_extension = file_name.split(".")[-1]
    return f"galleries/{instance.gallery.slug}/{instance.slug}.{file_extension}"


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    sort_order = models.IntegerField()

    the_image = models.ImageField(
        null=False,
        blank=False,
        upload_to=gallery_image_upload_to,
        storage=OverwriteStorage(),
    )
    added_timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        kwargs = {"gallery_slug": self.gallery.slug, "slug": self.slug}
        return reverse("gallery:gallery_image", kwargs=kwargs)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("gallery", "slug")
