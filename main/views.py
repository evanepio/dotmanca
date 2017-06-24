import datetime

from django.views import generic

from news.models import NewsArticle


def get_age(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    try:
        birthday = datetime.date(today.year, birth_month, birth_day)
    except ValueError:
        # Raised when person was born on 29 February and the current
        # year is not a leap year.
        birthday = datetime.date(today.year, birth_month, birth_day - 1)

    if birthday > today:
        return today.year - birth_year - 1
    else:
        return today.year - birth_year


class HomePageView(generic.TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['news_articles'] = NewsArticle.objects.order_by('-published_datetime')[:3]
        return context


class AboutView(generic.TemplateView):
    template_name = "main/about.html"


class AboutChasView(generic.TemplateView):
    template_name = "main/about_chas.html"

    def get_context_data(self, **kwargs):
        context = super(AboutChasView, self).get_context_data(**kwargs)
        context['age'] = get_age(1980, 4, 21)
        return context


class AboutEvanView(generic.TemplateView):
    template_name = "main/about_evan.html"

    def get_context_data(self, **kwargs):
        context = super(AboutEvanView, self).get_context_data(**kwargs)
        context['age'] = get_age(1980, 12, 6)
        return context
