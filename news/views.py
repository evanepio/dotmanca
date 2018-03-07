from datetime import date

from django.views import generic

from .models import NewsArticle


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'news_articles'

    def get_queryset(self):
        return NewsArticle.published_articles.order_by('-published_date')


class ArticleView(generic.DetailView):
    model = NewsArticle
    template_name = 'news/article.html'

    def get_queryset(self):
        pub_date = date(self.kwargs.get('year'),
                        self.kwargs.get('month'),
                        self.kwargs.get('day'))

        query_set = super(ArticleView, self).get_queryset()\
            .filter(slug=self.kwargs.get('slug'))\
            .filter(published_date=pub_date)

        return query_set
