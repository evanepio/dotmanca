from django.urls import path

from . import views

app_name = "comics"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<slug:arc_slug>/<slug:slug>/", views.IssueView.as_view(), name="issue"),
    path(
        "<slug:arc_slug>/<slug:issue_slug>/<slug:slug>/",
        views.ComicPageView.as_view(),
        name="comic_page",
    ),
]
