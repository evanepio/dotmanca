from django.views import generic

from . import queries
from .models import Gallery, GalleryImage


class IndexView(generic.ListView):
    model = Gallery
    template_name = "gallery/index.html"
    context_object_name = "galleries"


class GalleryView(generic.DetailView):
    model = Gallery
    template_name = "gallery/gallery.html"


class GalleryImageView(generic.DetailView):
    model = GalleryImage
    template_name = "gallery/gallery_image.html"

    def get_queryset(self):
        query_set = super().get_queryset().filter(gallery__slug=self.kwargs.get("gallery_slug"))
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["previous"] = queries.get_previous_image(self.object)
        context["next"] = queries.get_next_image(self.object)

        return context
