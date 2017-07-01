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
