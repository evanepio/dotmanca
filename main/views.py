import datetime

from django.views import generic

from news.models import NewsArticle


def get_age(birthdate, today):
    try:
        birthday = datetime.date(today.year, birthdate.month, birthdate.day)
    except ValueError:
        # Raised when person was born on 29 February and the current
        # year is not a leap year.
        birthday = datetime.date(today.year, birthdate.month, birthdate.day - 1)

    if birthday > today:
        return today.year - birthdate.year - 1
    else:
        return today.year - birthdate.year


class HomePageView(generic.TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['news_articles'] = NewsArticle.published_articles.order_by('-published_datetime')[:3]
        return context


class AboutView(generic.TemplateView):
    template_name = "main/about.html"


class AboutChasView(generic.TemplateView):
    template_name = "main/about_chas.html"
    date_function = datetime.date.today

    def get_context_data(self, **kwargs):
        context = super(AboutChasView, self).get_context_data(**kwargs)
        birthdate = datetime.date(1980, 4, 21)
        today = self.date_function()
        context['age'] = get_age(birthdate, today)
        return context


class AboutEvanView(generic.TemplateView):
    template_name = "main/about_evan.html"
    date_function = datetime.date.today

    def get_context_data(self, **kwargs):
        context = super(AboutEvanView, self).get_context_data(**kwargs)
        birthdate = datetime.date(1980, 12, 6)
        today = self.date_function()
        context['age'] = get_age(birthdate, today)
        return context
