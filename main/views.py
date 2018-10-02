import datetime

from django.views import generic

from news.models import NewsArticle


def get_age(date_of_birth):
    today = datetime.date.today()
    return (
        today.year
        - date_of_birth.year
        - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    )


class HomePageView(generic.TemplateView):
    template_name = "main/home.html"

    @staticmethod
    def get_published_news_articles():
        return NewsArticle.published_articles.order_by("-published_date")

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["news_articles"] = self.get_published_news_articles()[:3]
        return context


class AboutView(generic.TemplateView):
    template_name = "main/about.html"


class AboutAgedView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        context = super(AboutAgedView, self).get_context_data(**kwargs)
        context["age"] = get_age(self.date_of_birth)
        return context


class AboutChasView(AboutAgedView):
    template_name = "main/about_chas.html"
    date_of_birth = datetime.date(1980, 4, 21)


class AboutEvanView(AboutAgedView):
    template_name = "main/about_evan.html"
    date_of_birth = datetime.date(1980, 12, 6)
