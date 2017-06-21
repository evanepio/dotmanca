from django.db import models


class NewsArticle(models.Model):
    headline = models.CharField(max_length=70)
    slug = models.SlugField(unique_for_date="published_datetime")
    published_datetime = models.DateTimeField()
    content = models.TextField(blank=True)

    def __str__(self):
        return self.headline
