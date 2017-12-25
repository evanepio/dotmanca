import datetime

from django.views import generic

from news.models import NewsArticle


def get_age(date_of_birth, today):
    try:
        birthday = datetime.date(today.year, date_of_birth.month, date_of_birth.day)
    except ValueError:
        # Raised when person was born on 29 February and the current year is not a leap year.
        birthday = datetime.date(today.year, date_of_birth.month, date_of_birth.day - 1)

    if birthday > today:
        return today.year - date_of_birth.year - 1
    else:
        return today.year - date_of_birth.year


class HomePageView(generic.TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['news_articles'] = NewsArticle.published_articles.order_by('-published_datetime')[:3]
        return context


class AboutView(generic.TemplateView):
    template_name = "main/about.html"


class AboutAgedView(generic.TemplateView):
    date_function = datetime.date.today
    date_of_birth = datetime.date(1980, 4, 21)

    def get_context_data(self, **kwargs):
        context = super(AboutAgedView, self).get_context_data(**kwargs)
        today = self.date_function()
        context['age'] = get_age(self.date_of_birth, today)
        return context


class AboutChasView(AboutAgedView):
    template_name = "main/about_chas.html"
    date_of_birth = datetime.date(1980, 4, 21)


class AboutEvanView(AboutAgedView):
    template_name = "main/about_evan.html"
    date_of_birth = datetime.date(1980, 12, 6)
