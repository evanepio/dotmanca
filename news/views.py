from django.shortcuts import render
from django.views import generic

from .models import NewsArticle


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'news_articles'

    def get_queryset(self):
        return NewsArticle.objects.order_by('-published_datetime')


class ArticleView(generic.DetailView):
    model = NewsArticle
    template_name = 'news/article.html'
