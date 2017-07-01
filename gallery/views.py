from django.views import generic

from .models import Gallery, GalleryImage


class IndexView(generic.ListView):
    model = Gallery
    template_name = 'gallery/index.html'
    context_object_name = 'galleries'


class GalleryView(generic.DetailView):
    model = Gallery
    template_name = 'gallery/gallery.html'
