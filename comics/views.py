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


class ComicPageView(generic.DetailView):
    model = GalleryImage
    template_name = "comics/comic_page.html"

    def get_queryset(self):
        query_set = (
            super().get_queryset().filter(issue__slug=self.kwargs.get("issue_slug"))
        )
        return query_set
