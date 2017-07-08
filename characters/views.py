from django.views import generic

from .models import Team


class IndexView(generic.ListView):
    model = Team
    template_name = 'characters/index.html'
    context_object_name = 'teams'

