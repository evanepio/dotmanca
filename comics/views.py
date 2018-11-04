from django.views import generic

from gallery.models import GalleryImage
from gallery import queries
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

    def __init__(self):
        super().__init__()
        self.issue = None

    def get_queryset(self):
        # Find Issue, then get gallery
        self.issue = Issue.objects.filter(arc__slug=self.kwargs.get("arc_slug")).get(
            slug=self.kwargs.get("issue_slug")
        )

        query_set = super().get_queryset().filter(gallery__id=self.issue.gallery.id)
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["issue"] = self.issue  # This is set in get_queryset()

        gallery = self.issue.gallery
        sort_order = self.object.sort_order
        context["next"] = queries.get_next_image(gallery, sort_order)
        context["previous"] = queries.get_previous_image(gallery, sort_order)

        return context
