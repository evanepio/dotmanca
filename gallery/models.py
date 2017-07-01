from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    added_timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField()

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('gallery:gallery', kwargs=kwargs)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    sort_order = models.IntegerField()

    the_image = models.ImageField(null=False, blank=False)
    added_timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('gallery', 'slug')
