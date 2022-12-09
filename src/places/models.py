from django.db import models
from django.urls import reverse


def place_image_upload_to(instance, file_name):
    file_extension = file_name.split(".")[-1]
    return f"places/{instance.slug}.{file_extension}"


class Place(models.Model):
    name = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    slug = models.SlugField()
    description = models.TextField(blank=True)
    the_image = models.ImageField(
        blank=True,
        null=True,
        upload_to=place_image_upload_to,
    )

    def get_absolute_url(self):
        kwargs = {"slug": self.slug}
        return reverse("places:place", kwargs=kwargs)

    def __str__(self):
        return f"{self.name}"
