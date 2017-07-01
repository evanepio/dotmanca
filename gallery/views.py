from django.views import generic

from .models import Gallery


class IndexView(generic.ListView):
    model = Gallery
    template_name = 'gallery/index.html'
    context_object_name = 'galleries'
