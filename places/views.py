from django.views import generic

from .models import Place


class IndexView(generic.ListView):
    model = Place
    template_name = 'places/index.html'
    context_object_name = 'places'


class PlaceView(generic.DetailView):
    model = Place
    template_name = 'places/place.html'
