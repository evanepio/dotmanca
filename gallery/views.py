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

        gallery = self.object.gallery
        sort_order = self.object.sort_order

        context["previous"] = get_previous_image(gallery, sort_order)
        context["next"] = get_next_image(gallery, sort_order)

        return context


def get_previous_image(gallery, sort_order):
    return get_image_from_filtered_sorted_query_set(
        gallery, {"sort_order__lt": sort_order}, "-sort_order"
    )


def get_next_image(gallery, sort_order):
    return get_image_from_filtered_sorted_query_set(
        gallery, {"sort_order__gt": sort_order}, "sort_order"
    )


def get_image_from_filtered_sorted_query_set(gallery, filter_dict, sort_string):
    image = None

    try:
        # Reminder: the ** in front of the dict converts it to keyword args
        image = gallery.images.filter(**filter_dict).order_by(sort_string)[0]
    except IndexError:
        pass  # Don't worry about it

    return image
