from django.views import generic

from .models import Team, Character


class IndexView(generic.ListView):
    model = Team
    template_name = 'characters/index.html'
    context_object_name = 'teams'


class CharacterView(generic.DetailView):
    model = Character
    template_name = 'characters/character.html'

    def get_queryset(self):
        query_set = super(CharacterView, self).get_queryset().filter(team__slug=self.kwargs.get('team_slug'))
        return query_set
