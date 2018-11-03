from django.views import generic

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
        query_set = (
            super().get_queryset().filter(gallery__slug=self.kwargs.get("gallery_slug"))
        )
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        gallery_id = self.object.gallery_id
        sort_order = self.object.sort_order

        context["previous"] = get_previous_image(gallery_id, sort_order)
        context["next"] = get_next_image(gallery_id, sort_order)

        return context


def get_previous_image(gallery_id, sort_order):
    previous = None

    try:
        previous = (
            GalleryImage.objects.filter(gallery_id=gallery_id)
            .filter(sort_order__lt=sort_order)
            .order_by("sort_order")[0]
        )
    except IndexError:
        pass  # Don't worry about it

    return previous


def get_next_image(gallery_id, sort_order):
    previous = None

    try:
        previous = (
            GalleryImage.objects.filter(gallery_id=gallery_id)
            .filter(sort_order__gt=sort_order)
            .order_by("sort_order")[0]
        )
    except IndexError:
        pass  # Don't worry about it

    return previous

