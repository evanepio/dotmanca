from django.views import generic

from .models import Arc, Issue


class IndexView(generic.ListView):
    model = Arc
    template_name = 'comics/index.html'
    context_object_name = 'arcs'


