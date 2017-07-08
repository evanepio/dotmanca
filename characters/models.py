from django.db import models
from django.urls import reverse

from gallery.models import GalleryImage


class Team(models.Model):
    name = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    slug = models.SlugField(unique=True)
    the_image = models.ForeignKey(GalleryImage, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return F'{self.name} (Team)'

    class Meta:
        ordering = ('sort_order',)


class Character(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    slug = models.SlugField()
    the_image = models.ForeignKey(GalleryImage, blank=True, null=True)
    vital_stats = models.TextField(blank=True)
    backstory = models.TextField(blank=True)

    # def get_absolute_url(self):
    #     return ('character_view', (), {'slug': self.slug, })

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('sort_order',)
        unique_together = ('team', 'slug')
