from django.conf.urls import url

from . import views

app_name = 'characters'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<team_slug>[-\w]+)/(?P<slug>[-\w]+)/$', views.CharacterView.as_view(), name='character'),
]
