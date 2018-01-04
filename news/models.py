from datetime import date

from django.db import models
from django.urls import reverse


class PublishedArticlesManager(models.Manager):
    def get_queryset(self):
        today = date.today()
        return super(PublishedArticlesManager, self).get_queryset().filter(published_date__lte=today)


class NewsArticle(models.Model):
    headline = models.CharField(max_length=70)
    slug = models.SlugField(unique_for_date="published_date")
    published_date = models.DateField()
    content = models.TextField(blank=True)

    objects = models.Manager()
    published_articles = PublishedArticlesManager()

    def get_absolute_url(self):
        kwargs = {'year': str(self.published_date.year),
                  'month': str(self.published_date.month).zfill(2),
                  'day': str(self.published_date.day).zfill(2),
                  'slug': self.slug}

        return reverse('news:article', kwargs=kwargs)

    def __str__(self):
        return F"{self.published_date:%B %d, %Y} - {self.headline}"
