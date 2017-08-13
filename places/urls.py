from django.conf.urls import url

from . import views

app_name = 'places'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.PlaceView.as_view(), name='place'),
]
