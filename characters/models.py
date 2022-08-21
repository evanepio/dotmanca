from django.db import models
from django.urls import reverse

from gallery.models import GalleryImage


class Team(models.Model):
    name = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    slug = models.SlugField(unique=True)
    the_image = models.ForeignKey(
        GalleryImage, on_delete=models.CASCADE, blank=True, null=True
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} (Team)"

    class Meta:
        ordering = ("sort_order",)


def character_image_upload_to(instance, file_name):
    file_extension = file_name.split(".")[-1]
    return f"characters/{instance.team.slug}/{instance.slug}.{file_extension}"


class Character(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    slug = models.SlugField()
    the_image = models.ImageField(
        blank=True,
        null=True,
        upload_to=character_image_upload_to,
    )
    vital_stats = models.TextField(blank=True)
    backstory = models.TextField(blank=True)

    def get_absolute_url(self):
        kwargs = {"team_slug": self.team.slug, "slug": self.slug}
        return reverse("characters:character", kwargs=kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("sort_order",)
        unique_together = ("team", "slug")
