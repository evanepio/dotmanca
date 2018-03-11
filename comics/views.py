from django.views import generic

from .models import Arc, Issue


class IndexView(generic.ListView):
    model = Arc
    template_name = 'comics/index.html'
    context_object_name = 'arcs'


class IssueView(generic.DetailView):
    model = Issue
    template_name = 'comics/issue.html'
