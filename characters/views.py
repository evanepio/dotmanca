from django.views import generic

from .models import Character, Team


class IndexView(generic.ListView):
    model = Team
    template_name = "characters/index.html"
    context_object_name = "teams"


class CharacterView(generic.DetailView):
    model = Character
    template_name = "characters/character.html"

    def get_queryset(self):
        # Because team_slug and character slug are unique together, we'll need
        # to filter by team_slug provided by the URL, then the view can perform
        # its regular, configured logic inherited from generic.DetailView
        query_set = (
            super(CharacterView, self)
            .get_queryset()
            .filter(team__slug=self.kwargs.get("team_slug"))
        )
        return query_set
