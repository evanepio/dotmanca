from django.db import models

# Create your models here.


class NewsArticle(models.Model):
    headline = models.CharField(max_length=70)
    slug = models.SlugField()
    published_datetime = models.DateTimeField()
    published = models.BooleanField()
    content = models.TextField(blank=True)

    def __str__(self):
        return self.headline
