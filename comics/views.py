from django.views import generic

from gallery.models import GalleryImage
from .models import Arc, Issue


class IndexView(generic.ListView):
    model = Arc
    template_name = "comics/index.html"
    context_object_name = "arcs"


class IssueView(generic.DetailView):
    model = Issue
    template_name = "comics/issue.html"

    def get_queryset(self):
        query_set = super().get_queryset().filter(arc__slug=self.kwargs.get("arc_slug"))
        return query_set


class ComicPageView(generic.DetailView):
    model = GalleryImage
    template_name = "comics/comic_page.html"

    def get_queryset(self):
        # Find Issue, then get gallery
        self.issue = Issue.objects.filter(arc__slug=self.kwargs.get("arc_slug")).get(
            slug=self.kwargs.get("issue_slug")
        )

        query_set = super().get_queryset().filter(gallery__id=self.issue.gallery.id)
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["issue"] = self.issue  # Set in get_queryset()

        return context
