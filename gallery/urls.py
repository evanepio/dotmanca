from django.conf.urls import url

from . import views

app_name = 'gallery'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.GalleryView.as_view(), name='gallery'),
]
